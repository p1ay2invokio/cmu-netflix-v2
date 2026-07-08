import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://library.cmu.ac.th',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1',
    'Authorization': 'sEvIAKOMTCWa1EIo52LqzwlD6GYOB5ht',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://library.cmu.ac.th/',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Priority': 'u=3, i',
    'Connection': 'keep-alive',
}

response = requests.get(
    'https://cloud-3001.lib.cmu.ac.th/passport/mobile/token/DLCR7qo3iMSRAwzThlDXjydIzzgJLM',
    headers=headers,
    verify=False
)

print(response.text)