import tkinter as tk
from tkinter import messagebox
import requests
import urllib3
import json
import datetime
import webbrowser
import os
import sys
import ctypes
import customtkinter as ctk
from PIL import Image

# Disable InsecureRequestWarning warnings from urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

# Default cookies and headers from the original main.py
cookies = {
    '_ga_GYXSR60XKK': 'GS2.1.s1782284149$o3$g1$t1782284403$j57$l0$h0',
    'entra_data': '%7B%22cmuitaccount%22%3A%22rattanon_boonmata%40cmu.ac.th%22%2C%22cmuitaccount_name%22%3A%22rattanon_boonmata%22%2C%22firstname_EN%22%3A%22RATTANON%22%2C%22firstname_TH%22%3A%22%E0%B8%A3%E0%B8%B1%E0%B8%90%E0%B8%99%E0%B8%97%E0%B9%8C%22%2C%22is_cmu%22%3Atrue%2C%22itaccounttype_EN%22%3A%22Student%22%2C%22itaccounttype_TH%22%3A%22%E0%B8%99%E0%B8%B1%E0%B8%81%E0%B8%A8%E0%B8%B6%E0%B8%81%E0%B8%A9%E0%B8%B2%22%2C%22itaccounttype_id%22%3A%22StdAcc%22%2C%22lastname_EN%22%3A%22BOONMATA%22%2C%22lastname_TH%22%3A%22%E0%B8%A3%E0%B8%B1%E0%B8%90%E0%B8%99%E0%B8%97%E0%B9%8C%22%2C%22organization_code%22%3A%221%22%2C%22organization_name_EN%22%3A%22Faculty+of+Humanities%22%2C%22organization_name_TH%22%3A%22%E0%B8%84%E0%B8%93%E0%B8%B0%E0%B8%A1%E0%B8%99%E0%B8%B8%E0%B8%A9%E0%B8%A2%E0%B8%A8%E0%B8%B2%E0%B8%AA%E0%B8%95%E0%B8%A3%E0%B9%8C%22%2C%22picture%22%3A%22https%3A%2F%2Fapp.scmc.cmu.ac.th%2Fapi%2Fuser%2F88546%2Fpicture%3Ftoken%3DLhGI15gaH0D55F%22%2C%22prename_EN%22%3A%22%22%2C%22prename_TH%22%3A%22%22%2C%22prename_id%22%3A%22OTH%22%2C%22sex_id%22%3A%221%22%2C%22student_id%22%3A%22670110278%22%7D',
    'state': 'User',
    '_ga': 'GA1.1.628649458.1782273878',
}

headers = {
    'Accept': '*/*',
    'Content-Type': 'application/json',
    'Sec-Fetch-Site': 'same-site',
    'Origin': 'https://services.library.cmu.ac.th',
    'x-api-key': 'cmul-movie-api-xk9fP2mRtY8qN4vL',
    'Sec-Fetch-Mode': 'cors',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1',
    'Referer': 'https://services.library.cmu.ac.th/',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Priority': 'u=3, i',
    'Connection': 'keep-alive',
}

# --- Dynamic Font Loader (ctypes helper for Mac/Windows) ---

def load_font_macos(font_path):
    """Loads a TTF font dynamically into the process using macOS CoreText API."""
    try:
        coretext = ctypes.CDLL('/System/Library/Frameworks/ApplicationServices.framework/Frameworks/CoreText.framework/CoreText')
        corefoundation = ctypes.CDLL('/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation')
        
        corefoundation.CFStringCreateWithCString.restype = ctypes.c_void_p
        corefoundation.CFStringCreateWithCString.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_uint32]
        
        corefoundation.CFURLCreateWithFileSystemPath.restype = ctypes.c_void_p
        corefoundation.CFURLCreateWithFileSystemPath.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_long, ctypes.c_bool]
        
        coretext.CTFontManagerRegisterFontsForURL.restype = ctypes.c_bool
        coretext.CTFontManagerRegisterFontsForURL.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p]
        
        corefoundation.CFRelease.argtypes = [ctypes.c_void_p]
        
        path_bytes = os.path.abspath(font_path).encode('utf-8')
        cf_path = corefoundation.CFStringCreateWithCString(None, path_bytes, 0x08000100) # UTF-8 encoding
        cf_url = corefoundation.CFURLCreateWithFileSystemPath(None, cf_path, 0, False) # kCFURLPOSIXPathStyle
        
        success = coretext.CTFontManagerRegisterFontsForURL(cf_url, 1, None)
        
        corefoundation.CFRelease(cf_url)
        corefoundation.CFRelease(cf_path)
        return success
    except Exception as e:
        print(f"Error registering font on macOS: {e}")
        return False

def load_font_windows(font_path):
    """Loads a TTF font dynamically into the process using Windows GDI32 API."""
    try:
        gdi32 = ctypes.WinDLL("gdi32.dll")
        return gdi32.AddFontResourceW(font_path) > 0
    except Exception:
        return False

def load_all_custom_fonts():
    """Finds all TTF files in the fonts/ subdirectory and registers them."""
    fonts_dir = resource_path("fonts")
    if os.path.exists(fonts_dir):
        for filename in os.listdir(fonts_dir):
            if filename.lower().endswith(".ttf"):
                font_file_path = os.path.join(fonts_dir, filename)
                if sys.platform == "darwin":
                    load_font_macos(font_file_path)
                elif sys.platform == "win32":
                    load_font_windows(font_file_path)

# Load fonts before starting GUI
load_all_custom_fonts()

# --- State Control Variables ---
claim_in_progress = False
countdown_active = False
countdown_target = None
actual_password = ""
password_hidden = True
json_visible = False

def get_next_wednesday_14():
    """Calculates the next Wednesday at 14:00:00 local time."""
    now = datetime.datetime.now()
    days_ahead = 2 - now.weekday()
    if days_ahead < 0:  # Past Wednesday this week
        days_ahead += 7
    elif days_ahead == 0:  # Today is Wednesday
        # Check if already past 14:00
        if now.time() >= datetime.time(14, 0, 0):
            days_ahead += 7  # Target next Wednesday
            
    target_date = now.date() + datetime.timedelta(days=days_ahead)
    target_datetime = datetime.datetime.combine(target_date, datetime.time(14, 0, 0))
    return target_datetime

def fetch_quota_status():
    """Fetches claim quota stats from the server and updates UI."""
    lbl_stats.configure(text="สิทธิ์ว่าง: --/--", text_color="#71717a")
    root.update()
    
    try:
        response = requests.get(
            'https://datagateway.library.cmu.ac.th/api/movie-streaming/claim/stats',
            cookies=cookies,
            headers=headers,
            verify=False,
            timeout=8
        )
        
        data = response.json()
        if data.get("status") is True:
            available = data.get("available", 0)
            claimed = data.get("claimed", 0)
            total = data.get("total", 100)
            
            lbl_stats.configure(
                text=f"สิทธิ์ว่าง: {available} / {total}",
                text_color="#10b981" if available > 0 else "#ef4444"
            )
        else:
            lbl_stats.configure(text="สิทธิ์ว่าง: ล้มเหลว", text_color="#ef4444")
    except Exception:
        lbl_stats.configure(text="สิทธิ์ว่าง: ออฟไลน์", text_color="#ef4444")

def send_claim_request():
    global claim_in_progress
    if claim_in_progress:
        return
        
    cmuitaccount = entry_cmuitaccount.get().strip()
    phone = entry_phone.get().strip()
    
    # Simple Validation
    if not cmuitaccount or not phone:
        messagebox.showwarning("Warning", "Please fill in all fields")
        return
        
    claim_in_progress = True
    btn_submit.configure(text="PROCESSING...", fg_color="#5a0b0e", state="disabled")
    root.update()
    
    json_data = {
        'cmuitaccount': cmuitaccount,
        'phone': phone,
    }
    
    try:
        response = requests.post(
            'https://datagateway.library.cmu.ac.th/api/movie-streaming/claim',
            cookies=cookies,
            headers=headers,
            json=json_data,
            verify=False,
            timeout=15
        )
        
        # Display response
        txt_response.configure(state="normal")
        txt_response.delete("1.0", tk.END)
        try:
            parsed_json = json.loads(response.text)
            pretty_json = json.dumps(parsed_json, indent=4, ensure_ascii=False)
            txt_response.insert(tk.END, pretty_json)
            
            # Check for Success
            if response.status_code == 200 and parsed_json.get("status") is True:
                account = parsed_json.get("account", {})
                email = account.get("EmailAddress", "N/A")
                password = account.get("Password", "N/A")
                pin = parsed_json.get("pincode", {}).get("PinCode") or account.get("PinCode") or "N/A"
                profile = parsed_json.get("profile_no", "1")
                exp_date = account.get("ExpireDate", "")
                
                # Format Expiry
                if exp_date:
                    readable_date = exp_date.split("T")[0]
                else:
                    readable_date = "ไม่มีกำหนด"
                
                # Populate GUI Results
                lbl_res_email.configure(text=email)
                
                global actual_password, password_hidden
                actual_password = password
                lbl_res_pwd.configure(text="••••••••")
                btn_show_pwd.configure(text="👁️ Show")
                password_hidden = True
                
                lbl_res_profile.configure(text=f"Profile {profile}")
                lbl_res_pin.configure(text=str(pin))
                lbl_res_expiry.configure(text=f"สิทธิ์หมดอายุวันที่: {readable_date}")
                
                # Prettify raw JSON in result bottom box
                txt_res_json.configure(state="normal")
                txt_res_json.delete("1.0", tk.END)
                txt_res_json.insert(tk.END, pretty_json)
                txt_res_json.configure(state="disabled")
                
                # Hide Form, Show Results layout
                form_frame.pack_forget()
                info_frame.pack_forget()
                lbl_response_header.pack_forget()
                txt_response.pack_forget()
                
                result_frame.pack(fill="x", pady=0)
                
                # Trigger Alert Popup
                success_msg = (
                    "🎉 รับสิทธิ์ Netflix สำเร็จเรียบร้อยแล้ว!\n\n"
                    f"📧 อีเมล: {email}\n"
                    f"🔑 รหัสผ่าน: {password}\n"
                    f"👤 โปรไฟล์: Profile {profile}\n"
                    f"🔒 รหัสล็อก PIN: {pin}"
                )
                messagebox.showinfo("ทำรายการสำเร็จ", success_msg)
                fetch_quota_status()
            else:
                error_msg = parsed_json.get("message") or parsed_json.get("detail") or "เกิดข้อผิดพลาดในการรับสิทธิ์"
                messagebox.showerror("ทำรายการไม่สำเร็จ", f"ข้อผิดพลาด: {error_msg}")
                
        except ValueError:
            txt_response.insert(tk.END, response.text)
            messagebox.showerror("เกิดข้อผิดพลาด", "ข้อมูลตอบกลับจากเซิร์ฟเวอร์มีรูปแบบไม่ถูกต้อง")
            
        txt_response.configure(state="disabled")
        
        # Print to terminal
        print(response.text)
        
    except Exception as e:
        messagebox.showerror("Error", f"Connection failed: {str(e)}")
    finally:
        claim_in_progress = False
        btn_submit.configure(text="CLAIM NOW  ▶", fg_color=ACCENT, state="normal")

# --- Auto-Claim Countdown Functions ---

def start_countdown_mode():
    global countdown_target, countdown_active
    cmuitaccount = entry_cmuitaccount.get().strip()
    phone = entry_phone.get().strip()
    
    if not cmuitaccount or not phone:
        messagebox.showwarning("Warning", "Please fill in all fields")
        return
        
    countdown_target = get_next_wednesday_14()
    countdown_active = True
    
    # Lock Inputs
    entry_cmuitaccount.configure(state="disabled")
    entry_phone.configure(state="disabled")
    chk_auto.configure(state="disabled")
    
    tick_countdown()

def cancel_countdown():
    global countdown_active
    countdown_active = False
    
    # Unlock Inputs
    entry_cmuitaccount.configure(state="normal")
    entry_phone.configure(state="normal")
    chk_auto.configure(state="normal")
    
    btn_submit.configure(text="CLAIM NOW  ▶", fg_color=ACCENT)
    lbl_timer_status.configure(text="")

def tick_countdown():
    global countdown_active, countdown_target
    if not countdown_active:
        return
        
    now = datetime.datetime.now()
    diff = countdown_target - now
    
    if diff.total_seconds() <= 0:
        lbl_timer_status.configure(text="🔥 Triggering claim API now!")
        
        entry_cmuitaccount.configure(state="normal")
        entry_phone.configure(state="normal")
        chk_auto.configure(state="normal")
        
        countdown_active = False
        lbl_timer_status.configure(text="")
        
        send_claim_request()
        return
        
    # Calculate countdown strings
    tot_seconds = int(diff.total_seconds())
    days, remainder = divmod(tot_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    if days > 0:
        time_str = f"{days}วัน {hours:02d}:{minutes:02d}:{seconds:02d}"
    else:
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        
    btn_submit.configure(text=f"CANCEL WAITING ({time_str})", fg_color="#27272a")
    
    target_str = countdown_target.strftime("%Y-%m-%d %H:%M:%S")
    lbl_timer_status.configure(text=f"ตั้งเวลายิงอัตโนมัติรอบ: {target_str}\n(กดปุ่มสีเทาเพื่อยกเลิก)")
    
    # Refresh stats occasionally while counting down (every 60 seconds)
    if tot_seconds % 60 == 0:
        fetch_quota_status()
        
    # Schedule next tick in 1 second
    root.after(1000, tick_countdown)

# --- GUI Clipboard & Helpers ---

def copy_val(value, field_name):
    root.clipboard_clear()
    root.clipboard_append(value)
    lbl_result_status.configure(text=f"คัดลอก {field_name} สำเร็จ! ✔️", text_color="#10b981")
    root.after(2000, lambda: lbl_result_status.configure(text="", text_color="#00b0ff"))

def toggle_password():
    global password_hidden
    if password_hidden:
        lbl_res_pwd.configure(text=actual_password)
        btn_show_pwd.configure(text="👁️ Hide")
        password_hidden = False
    else:
        lbl_res_pwd.configure(text="••••••••")
        btn_show_pwd.configure(text="👁️ Show")
        password_hidden = True

def open_netflix():
    webbrowser.open("https://netflix.com")

def toggle_raw_json():
    global json_visible
    if json_visible:
        txt_res_json.pack_forget()
        btn_toggle_json.configure(text="ดูข้อมูลดิบ Raw Response JSON ▼")
        json_visible = False
    else:
        txt_res_json.pack(fill="both", expand=True, pady=(5, 0))
        btn_toggle_json.configure(text="ซ่อนข้อมูลดิบ Raw Response JSON ▲")
        json_visible = True

def reset_to_form():
    """Hides results frame, and shows Form inputs screen again."""
    result_frame.pack_forget()
    
    form_frame.pack(fill="x", pady=0)
    info_frame.pack(fill="x", pady=(0, 20))
    lbl_response_header.pack(anchor="w", pady=(0, 6))
    txt_response.pack(fill="both", expand=True)

# --- UI Theme Color Constants ---
FONT_FAMILY = "Kanit"

BG_DARK = "#09090b"       # zinc-950 (Deep dark background)
BG_CARD = "#18181b"       # zinc-900 (Response area & info background)
BG_ENTRY = "#27272a"      # zinc-800 (Flat entry field background)
FG_TEXT = "#f4f4f5"       # zinc-100 (Primary text)
FG_SUB = "#71717a"        # zinc-500 (Subtitles and secondary label text)
FG_INFO_TEXT = "#a1a1aa"   # zinc-400 (Body text inside info card)
ACCENT = "#e50914"        # Netflix Red
ACCENT_HOVER = "#b80710"  # Crimson dark red on hover

# Configure CustomTkinter appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# --- Initialize Window ---
root = ctk.CTk()
root.title("CMU Netflix Claim")
root.geometry("420x680")
root.configure(fg_color=BG_DARK)
root.resizable(False, False)

# Main Container
main_frame = ctk.CTkFrame(root, fg_color=BG_DARK)
main_frame.pack(fill="both", expand=True, padx=25, pady=25)

# Developer Credit Footer (Packed FIRST with side="bottom" so it is always visible at the bottom)
lbl_dev = ctk.CTkLabel(
    main_frame,
    text="Software Architecture Rattanon Boonmata \n Implementation assisted by Claude Opus 4.8",
    font=ctk.CTkFont(family=FONT_FAMILY, size=9),
    fg_color=BG_DARK,
    text_color=FG_SUB
)
lbl_dev.pack(side="bottom", pady=(10, 0))

# Header Section
header_frame = ctk.CTkFrame(main_frame, fg_color=BG_DARK)
header_frame.pack(fill="x", pady=(0, 20))

# Header Title (Left)
title_frame = ctk.CTkFrame(header_frame, fg_color=BG_DARK)
title_frame.pack(side="left")

title_row = ctk.CTkFrame(title_frame, fg_color=BG_DARK)
title_row.pack(anchor="w")

# Try loading the logo image
logo_path = resource_path(os.path.join("logo", "Chiang_Mai_University.svg.png"))
logo_img = None
if os.path.exists(logo_path):
    try:
        img = Image.open(logo_path)
        logo_img = ctk.CTkImage(light_image=img, dark_image=img, size=(28, 28))
    except Exception as e:
        print(f"Error loading logo: {e}")

if logo_img:
    lbl_logo = ctk.CTkLabel(title_row, image=logo_img, text="", fg_color=BG_DARK)
    lbl_logo.image = logo_img  # Keep reference
    lbl_logo.pack(side="left", padx=(0, 8))

lbl_title = ctk.CTkLabel(
    title_row,
    text="CMU NETFLIX",
    font=ctk.CTkFont(family=FONT_FAMILY, size=18, weight="bold"),
    fg_color=BG_DARK,
    text_color=FG_TEXT
)
lbl_title.pack(side="left")

lbl_desc = ctk.CTkLabel(
    title_frame,
    text="Claim movie streaming account.",
    font=ctk.CTkFont(family=FONT_FAMILY, size=9),
    fg_color=BG_DARK,
    text_color=FG_SUB
)
lbl_desc.pack(anchor="w", pady=(2, 0))

# Quota Status (Right)
stats_panel = ctk.CTkFrame(header_frame, fg_color=BG_DARK)
stats_panel.pack(side="right", anchor="ne")

lbl_stats = ctk.CTkLabel(
    stats_panel,
    text="สิทธิ์ว่าง: --/--",
    font=ctk.CTkFont(family=FONT_FAMILY, size=9, weight="bold"),
    fg_color=BG_DARK,
    text_color="#00b0ff"
)
lbl_stats.pack(side="left", padx=(0, 5), pady=2)

btn_refresh = ctk.CTkButton(
    stats_panel,
    text="🔄",
    font=ctk.CTkFont(family=FONT_FAMILY, size=10),
    fg_color=BG_CARD,
    hover_color="#27272a",
    text_color=FG_TEXT,
    width=28,
    height=26,
    corner_radius=6,
    command=fetch_quota_status
)
btn_refresh.pack(side="left")

# ======================================================
# FORM SCREEN (Initially Shown)
# ======================================================
form_frame = ctk.CTkFrame(main_frame, fg_color=BG_DARK)
form_frame.pack(fill="x", pady=0)

# Input 1: Account
lbl_cmuitaccount = ctk.CTkLabel(
    form_frame,
    text="CMU IT Account",
    font=ctk.CTkFont(family=FONT_FAMILY, size=9, weight="bold"),
    fg_color=BG_DARK,
    text_color=FG_SUB
)
lbl_cmuitaccount.pack(anchor="w", pady=(0, 5))

entry_cmuitaccount = ctk.CTkEntry(
    form_frame,
    font=ctk.CTkFont(family=FONT_FAMILY, size=11),
    fg_color=BG_ENTRY,
    text_color=FG_TEXT,
    border_width=0,
    corner_radius=8,
    height=34
)
entry_cmuitaccount.pack(fill="x", pady=(0, 16))
entry_cmuitaccount.insert(0, "santiphap_muenjit@cmu.ac.th")

# Input 2: Phone
lbl_phone = ctk.CTkLabel(
    form_frame,
    text="Phone Number",
    font=ctk.CTkFont(family=FONT_FAMILY, size=9, weight="bold"),
    fg_color=BG_DARK,
    text_color=FG_SUB
)
lbl_phone.pack(anchor="w", pady=(0, 5))

entry_phone = ctk.CTkEntry(
    form_frame,
    font=ctk.CTkFont(family=FONT_FAMILY, size=11),
    fg_color=BG_ENTRY,
    text_color=FG_TEXT,
    border_width=0,
    corner_radius=8,
    height=34
)
entry_phone.pack(fill="x", pady=(0, 15))
entry_phone.insert(0, "0610107102")

# Checkbox for Auto-Claim Mode
var_auto = tk.IntVar(value=1)
chk_auto = ctk.CTkCheckBox(
    main_frame,
    text="ตั้งเวลายิงสมัครอัตโนมัติ (วันพุธ 14.00 น.)",
    variable=var_auto,
    font=ctk.CTkFont(family=FONT_FAMILY, size=9, weight="bold"),
    fg_color=ACCENT,
    hover_color=ACCENT_HOVER,
    text_color=FG_TEXT,
    border_width=1,
    corner_radius=4
)
chk_auto.pack(anchor="w", pady=(0, 12))

# Submit Button / Action Handler
btn_submit = ctk.CTkButton(
    main_frame,
    text="CLAIM NOW  ▶",
    font=ctk.CTkFont(family=FONT_FAMILY, size=11, weight="bold"),
    fg_color=ACCENT,
    hover_color=ACCENT_HOVER,
    text_color="#ffffff",
    height=40,
    corner_radius=10,
    command=lambda: on_submit_click(None)
)
btn_submit.pack(fill="x", pady=(0, 5))

# Auto Claim Countdown Status Label
lbl_timer_status = ctk.CTkLabel(
    main_frame,
    text="",
    font=ctk.CTkFont(family=FONT_FAMILY, size=8, weight="bold"),
    fg_color=BG_DARK,
    text_color="#00b0ff"
)
lbl_timer_status.pack(fill="x", pady=(0, 15))

# Click handler helper
def on_submit_click(e):
    if countdown_active:
        cancel_countdown()
    elif var_auto.get() == 1:
        start_countdown_mode()
    else:
        send_claim_request()

# Info Frame (CMU Library guidelines)
info_frame = ctk.CTkFrame(main_frame, fg_color=BG_CARD, corner_radius=12)
info_frame.pack(fill="x", pady=(0, 20))

lbl_info_title = ctk.CTkLabel(
    info_frame,
    text="📌 ข้อมูลและเงื่อนไขบริการจองสิทธิ์ Netflix",
    font=ctk.CTkFont(family=FONT_FAMILY, size=9, weight="bold"),
    fg_color=BG_CARD,
    text_color=FG_TEXT
)
lbl_info_title.pack(anchor="w", padx=12, pady=(12, 4))

info_rules = (
    "• ลงทะเบียนได้ทุกวันพุธ เริ่มเวลา 14.00 น.\n"
    "• ใช้บริการได้นานสูงสุด 7 วัน (จำกัดสัปดาห์ละ 100 สิทธิ์)\n"
    "• รองรับการเข้าชมผ่านโทรศัพท์มือถือ หรือ Tablet เท่านั้น\n"
    "• เฉพาะนักศึกษาและบุคลากร มหาวิทยาลัยเชียงใหม่\n"
)

lbl_info_desc = ctk.CTkLabel(
    info_frame,
    text=info_rules,
    font=ctk.CTkFont(family=FONT_FAMILY, size=9),
    fg_color=BG_CARD,
    text_color=FG_INFO_TEXT,
    justify="left",
    anchor="w"
)
lbl_info_desc.pack(anchor="w", padx=12, pady=(0, 12))

# API Response Section (For errors/debugging)
lbl_response_header = ctk.CTkLabel(
    main_frame,
    text="API RESPONSE",
    font=ctk.CTkFont(family=FONT_FAMILY, size=8, weight="bold"),
    fg_color=BG_DARK,
    text_color=FG_SUB
)
lbl_response_header.pack(anchor="w", pady=(0, 6))

# Read-only Text Box for Output
txt_response = ctk.CTkTextbox(
    main_frame,
    font=("Courier New", 9),
    fg_color=BG_CARD,
    text_color="#10b981",
    border_width=0,
    corner_radius=12
)
txt_response.pack(fill="both", expand=True)


# ======================================================
# RESULTS SCREEN (Shown only on successful claim)
# ======================================================
result_frame = ctk.CTkFrame(main_frame, fg_color=BG_DARK)

# Success Badge
lbl_success_badge = ctk.CTkLabel(
    result_frame,
    text="CLAIM SUCCESSFUL 🎉",
    font=ctk.CTkFont(family=FONT_FAMILY, size=11, weight="bold"),
    fg_color="#10b981",
    text_color="#ffffff",
    height=32,
    corner_radius=8
)
lbl_success_badge.pack(fill="x", pady=(0, 16))

# Result status notification label (e.g. copied clipboard alerts)
lbl_result_status = ctk.CTkLabel(
    result_frame,
    text="",
    font=ctk.CTkFont(family=FONT_FAMILY, size=9, weight="bold"),
    fg_color=BG_DARK,
    text_color="#00b0ff"
)
lbl_result_status.pack(pady=(0, 8))

# Email Card
card_email = ctk.CTkFrame(result_frame, fg_color=BG_CARD, corner_radius=12)
card_email.pack(fill="x", pady=(0, 8))
lbl_email_title = ctk.CTkLabel(card_email, text="NETFLIX EMAIL / บัญชีใช้งาน", font=ctk.CTkFont(family=FONT_FAMILY, size=8, weight="bold"), fg_color=BG_CARD, text_color=FG_SUB)
lbl_email_title.pack(anchor="w", padx=12, pady=(10, 0))

email_inner = ctk.CTkFrame(card_email, fg_color=BG_CARD)
email_inner.pack(fill="x", padx=12, pady=(0, 10))
lbl_res_email = ctk.CTkLabel(email_inner, text="email@example.com", font=ctk.CTkFont(family=FONT_FAMILY, size=11, weight="bold"), fg_color=BG_CARD, text_color=FG_TEXT)
lbl_res_email.pack(side="left")

btn_copy_email = ctk.CTkButton(email_inner, text="📋 Copy", font=ctk.CTkFont(family=FONT_FAMILY, size=8, weight="bold"), fg_color=BG_ENTRY, hover_color="#3f3f46", text_color=FG_TEXT, width=54, height=24, corner_radius=6, command=lambda: copy_val(lbl_res_email.cget("text"), "อีเมล"))
btn_copy_email.pack(side="right")

# Password Card
card_pwd = ctk.CTkFrame(result_frame, fg_color=BG_CARD, corner_radius=12)
card_pwd.pack(fill="x", pady=(0, 8))
lbl_pwd_title = ctk.CTkLabel(card_pwd, text="NETFLIX PASSWORD / รหัสผ่าน", font=ctk.CTkFont(family=FONT_FAMILY, size=8, weight="bold"), fg_color=BG_CARD, text_color=FG_SUB)
lbl_pwd_title.pack(anchor="w", padx=12, pady=(10, 0))

pwd_inner = ctk.CTkFrame(card_pwd, fg_color=BG_CARD)
pwd_inner.pack(fill="x", padx=12, pady=(0, 10))
lbl_res_pwd = ctk.CTkLabel(pwd_inner, text="••••••••", font=ctk.CTkFont(family=FONT_FAMILY, size=11, weight="bold"), fg_color=BG_CARD, text_color=FG_TEXT)
lbl_res_pwd.pack(side="left")

pwd_actions = ctk.CTkFrame(pwd_inner, fg_color=BG_CARD)
pwd_actions.pack(side="right")

btn_show_pwd = ctk.CTkButton(pwd_actions, text="👁️ Show", font=ctk.CTkFont(family=FONT_FAMILY, size=8, weight="bold"), fg_color=BG_ENTRY, hover_color="#3f3f46", text_color=FG_TEXT, width=54, height=24, corner_radius=6, command=toggle_password)
btn_show_pwd.pack(side="left", padx=(0, 4))

btn_copy_pwd = ctk.CTkButton(pwd_actions, text="📋 Copy", font=ctk.CTkFont(family=FONT_FAMILY, size=8, weight="bold"), fg_color=BG_ENTRY, hover_color="#3f3f46", text_color=FG_TEXT, width=54, height=24, corner_radius=6, command=lambda: copy_val(actual_password, "รหัสผ่าน"))
btn_copy_pwd.pack(side="left")

# Profile and PIN
details_row = ctk.CTkFrame(result_frame, fg_color=BG_DARK)
details_row.pack(fill="x", pady=(0, 10))

# Profile sub-card
card_profile = ctk.CTkFrame(details_row, fg_color=BG_CARD, corner_radius=12)
card_profile.pack(side="left", fill="both", expand=True, padx=(0, 4))
lbl_profile_title = ctk.CTkLabel(card_profile, text="PROFILE / โปรไฟล์", font=ctk.CTkFont(family=FONT_FAMILY, size=8, weight="bold"), fg_color=BG_CARD, text_color=FG_SUB)
lbl_profile_title.pack(anchor="center", pady=(10, 0))
lbl_res_profile = ctk.CTkLabel(card_profile, text="Profile 1", font=ctk.CTkFont(family=FONT_FAMILY, size=13, weight="bold"), fg_color=BG_CARD, text_color=ACCENT)
lbl_res_profile.pack(anchor="center", pady=(4, 10))

# PIN sub-card
card_pin = ctk.CTkFrame(details_row, fg_color=BG_CARD, corner_radius=12)
card_pin.pack(side="right", fill="both", expand=True, padx=(4, 0))
lbl_pin_title = ctk.CTkLabel(card_pin, text="PIN CODE / รหัสล็อก", font=ctk.CTkFont(family=FONT_FAMILY, size=8, weight="bold"), fg_color=BG_CARD, text_color=FG_SUB)
lbl_pin_title.pack(anchor="center", pady=(10, 0))

pin_inner = ctk.CTkFrame(card_pin, fg_color=BG_CARD)
pin_inner.pack(anchor="center", pady=(2, 10))
lbl_res_pin = ctk.CTkLabel(pin_inner, text="9999", font=ctk.CTkFont(family=FONT_FAMILY, size=13, weight="bold"), fg_color=BG_CARD, text_color="#00b0ff")
lbl_res_pin.pack(side="left")

btn_copy_pin = ctk.CTkButton(pin_inner, text="📋", font=ctk.CTkFont(family=FONT_FAMILY, size=8), fg_color=BG_ENTRY, hover_color="#3f3f46", text_color=FG_TEXT, width=24, height=22, corner_radius=6, command=lambda: copy_val(lbl_res_pin.cget("text"), "PIN Code"))
btn_copy_pin.pack(side="left", padx=(6, 0))

# Expiry Box
card_expiry = ctk.CTkFrame(result_frame, fg_color=BG_CARD, corner_radius=12)
card_expiry.pack(fill="x", pady=(0, 15))
lbl_res_expiry = ctk.CTkLabel(
    card_expiry,
    text="สิทธิ์หมดอายุวันที่: 2026-07-01",
    font=ctk.CTkFont(family=FONT_FAMILY, size=9, weight="bold"),
    fg_color=BG_CARD,
    text_color="#ffb000"
)
lbl_res_expiry.pack(anchor="center", pady=10)

# Direct Launch Netflix Button
btn_launch = ctk.CTkButton(
    result_frame,
    text="▶️ OPEN NETFLIX",
    font=ctk.CTkFont(family=FONT_FAMILY, size=11, weight="bold"),
    fg_color="#ffffff",
    hover_color="#f4f4f5",
    text_color="#000000",
    height=40,
    corner_radius=10,
    command=open_netflix
)
btn_launch.pack(fill="x", pady=(0, 8))

# Back / Re-claim Button
btn_back = ctk.CTkButton(
    result_frame,
    text="ทำรายการใหม่ (BACK TO FORM)",
    font=ctk.CTkFont(family=FONT_FAMILY, size=9, weight="bold"),
    fg_color=BG_ENTRY,
    hover_color="#3f3f46",
    text_color=FG_TEXT,
    height=36,
    corner_radius=10,
    command=reset_to_form
)
btn_back.pack(fill="x", pady=(0, 10))

# Bottom JSON details
json_toggle_frame = ctk.CTkFrame(result_frame, fg_color=BG_DARK)
json_toggle_frame.pack(fill="both", expand=True, pady=(5, 0))

btn_toggle_json = ctk.CTkButton(
    json_toggle_frame,
    text="ดูข้อมูลดิบ Raw Response JSON ▼",
    font=ctk.CTkFont(family=FONT_FAMILY, size=8, weight="bold"),
    fg_color=BG_CARD,
    hover_color="#27272a",
    text_color=FG_SUB,
    height=26,
    corner_radius=6,
    command=toggle_raw_json
)
btn_toggle_json.pack(fill="x")

txt_res_json = ctk.CTkTextbox(
    json_toggle_frame,
    font=("Courier New", 8),
    fg_color=BG_CARD,
    text_color="#10b981",
    border_width=0,
    corner_radius=8,
    height=120
)



# Fetch Stats on Startup
root.after(150, fetch_quota_status)

root.mainloop()