import requests

def checkStatus():

    cookies = {
        'entra_data': '%7B%22cmuitaccount%22%3A%22rattanon_boonmata%40cmu.ac.th%22%2C%22cmuitaccount_name%22%3A%22rattanon_boonmata%22%2C%22firstname_EN%22%3A%22RATTANON%22%2C%22firstname_TH%22%3A%22%E0%B8%A3%E0%B8%B1%E0%B8%90%E0%B8%99%E0%B8%99%E0%B8%97%E0%B9%8C%22%2C%22is_cmu%22%3Atrue%2C%22itaccounttype_EN%22%3A%22Student%22%2C%22itaccounttype_TH%22%3A%22%E0%B8%99%E0%B8%B1%E0%B8%81%E0%B8%A8%E0%B8%B6%E0%B8%81%E0%B8%A9%E0%B8%B2%22%2C%22itaccounttype_id%22%3A%22StdAcc%22%2C%22lastname_EN%22%3A%22BOONMATA%22%2C%22lastname_TH%22%3A%22%E0%B8%9A%E0%B8%B8%E0%B8%8D%E0%B8%A1%E0%B8%B2%E0%B8%95%E0%B8%B2%22%2C%22organization_code%22%3A%221%22%2C%22organization_name_EN%22%3A%22Faculty+of+Humanities%22%2C%22organization_name_TH%22%3A%22%E0%B8%84%E0%B8%93%E0%B8%B0%E0%B8%A1%E0%B8%99%E0%B8%B8%E0%B8%A9%E0%B8%A2%E0%B8%A8%E0%B8%B2%E0%B8%AA%E0%B8%95%E0%B8%A3%E0%B9%8C%22%2C%22picture%22%3A%22https%3A%2F%2Fapp.scmc.cmu.ac.th%2Fapi%2Fuser%2F88546%2Fpicture%3Ftoken%3DLhGI15gaH0D55F%22%2C%22prename_EN%22%3A%22%22%2C%22prename_TH%22%3A%22%22%2C%22prename_id%22%3A%22OTH%22%2C%22sex_id%22%3A%221%22%2C%22student_id%22%3A%22670110278%22%7D',
        'state': 'User',
        '_ga_GYXSR60XKK': 'GS2.1.s1782284149$o3$g1$t1782284400$j60$l0$h0',
        '_ga': 'GA1.1.628649458.1782273878',
    }

    headers = {
        'Sec-Fetch-Site': 'same-site',
        'Accept': '*/*',
        'Origin': 'https://services.library.cmu.ac.th',
        'x-api-key': 'cmul-movie-api-xk9fP2mRtY8qN4vL',
        'Sec-Fetch-Mode': 'cors',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1',
        'Referer': 'https://services.library.cmu.ac.th/',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Priority': 'u=3, i',
        # 'Cookie': 'entra_data=%7B%22cmuitaccount%22%3A%22rattanon_boonmata%40cmu.ac.th%22%2C%22cmuitaccount_name%22%3A%22rattanon_boonmata%22%2C%22firstname_EN%22%3A%22RATTANON%22%2C%22firstname_TH%22%3A%22%E0%B8%A3%E0%B8%B1%E0%B8%90%E0%B8%99%E0%B8%99%E0%B8%97%E0%B9%8C%22%2C%22is_cmu%22%3Atrue%2C%22itaccounttype_EN%22%3A%22Student%22%2C%22itaccounttype_TH%22%3A%22%E0%B8%99%E0%B8%B1%E0%B8%81%E0%B8%A8%E0%B8%B6%E0%B8%81%E0%B8%A9%E0%B8%B2%22%2C%22itaccounttype_id%22%3A%22StdAcc%22%2C%22lastname_EN%22%3A%22BOONMATA%22%2C%22lastname_TH%22%3A%22%E0%B8%9A%E0%B8%B8%E0%B8%8D%E0%B8%A1%E0%B8%B2%E0%B8%95%E0%B8%B2%22%2C%22organization_code%22%3A%221%22%2C%22organization_name_EN%22%3A%22Faculty+of+Humanities%22%2C%22organization_name_TH%22%3A%22%E0%B8%84%E0%B8%93%E0%B8%B0%E0%B8%A1%E0%B8%99%E0%B8%B8%E0%B8%A9%E0%B8%A2%E0%B8%A8%E0%B8%B2%E0%B8%AA%E0%B8%95%E0%B8%A3%E0%B9%8C%22%2C%22picture%22%3A%22https%3A%2F%2Fapp.scmc.cmu.ac.th%2Fapi%2Fuser%2F88546%2Fpicture%3Ftoken%3DLhGI15gaH0D55F%22%2C%22prename_EN%22%3A%22%22%2C%22prename_TH%22%3A%22%22%2C%22prename_id%22%3A%22OTH%22%2C%22sex_id%22%3A%221%22%2C%22student_id%22%3A%22670110278%22%7D; state=User; _ga_GYXSR60XKK=GS2.1.s1782284149$o3$g1$t1782284400$j60$l0$h0; _ga=GA1.1.628649458.1782273878',
        'Connection': 'keep-alive',
    }
    

    response = requests.get(
        'https://datagateway.library.cmu.ac.th/api/movie-streaming/claim/status',
        cookies=cookies,
        headers=headers,
    )
    
def checkMe():
    
    cookies = {
        'entra_data': '%7B%22cmuitaccount%22%3A%22rattanon_boonmata%40cmu.ac.th%22%2C%22cmuitaccount_name%22%3A%22rattanon_boonmata%22%2C%22firstname_EN%22%3A%22RATTANON%22%2C%22firstname_TH%22%3A%22%E0%B8%A3%E0%B8%B1%E0%B8%90%E0%B8%99%E0%B8%99%E0%B8%97%E0%B9%8C%22%2C%22is_cmu%22%3Atrue%2C%22itaccounttype_EN%22%3A%22Student%22%2C%22itaccounttype_TH%22%3A%22%E0%B8%99%E0%B8%B1%E0%B8%81%E0%B8%A8%E0%B8%B6%E0%B8%81%E0%B8%A9%E0%B8%B2%22%2C%22itaccounttype_id%22%3A%22StdAcc%22%2C%22lastname_EN%22%3A%22BOONMATA%22%2C%22lastname_TH%22%3A%22%E0%B8%9A%E0%B8%B8%E0%B8%8D%E0%B8%A1%E0%B8%B2%E0%B8%95%E0%B8%B2%22%2C%22organization_code%22%3A%221%22%2C%22organization_name_EN%22%3A%22Faculty+of+Humanities%22%2C%22organization_name_TH%22%3A%22%E0%B8%84%E0%B8%93%E0%B8%B0%E0%B8%A1%E0%B8%99%E0%B8%B8%E0%B8%A9%E0%B8%A2%E0%B8%A8%E0%B8%B2%E0%B8%AA%E0%B8%95%E0%B8%A3%E0%B9%8C%22%2C%22picture%22%3A%22https%3A%2F%2Fapp.scmc.cmu.ac.th%2Fapi%2Fuser%2F88546%2Fpicture%3Ftoken%3DLhGI15gaH0D55F%22%2C%22prename_EN%22%3A%22%22%2C%22prename_TH%22%3A%22%22%2C%22prename_id%22%3A%22OTH%22%2C%22sex_id%22%3A%221%22%2C%22student_id%22%3A%22670110278%22%7D',
        'state': 'User',
        '_ga_GYXSR60XKK': 'GS2.1.s1782284149$o3$g1$t1782284400$j60$l0$h0',
        '_ga': 'GA1.1.628649458.1782273878',
    }

    headers = {
        'Sec-Fetch-Site': 'same-site',
        'Accept': '*/*',
        'Origin': 'https://services.library.cmu.ac.th',
        'x-api-key': 'cmul-movie-api-xk9fP2mRtY8qN4vL',
        'Sec-Fetch-Mode': 'cors',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1',
        'Referer': 'https://services.library.cmu.ac.th/',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Priority': 'u=3, i',
        # 'Cookie': 'entra_data=%7B%22cmuitaccount%22%3A%22rattanon_boonmata%40cmu.ac.th%22%2C%22cmuitaccount_name%22%3A%22rattanon_boonmata%22%2C%22firstname_EN%22%3A%22RATTANON%22%2C%22firstname_TH%22%3A%22%E0%B8%A3%E0%B8%B1%E0%B8%90%E0%B8%99%E0%B8%99%E0%B8%97%E0%B9%8C%22%2C%22is_cmu%22%3Atrue%2C%22itaccounttype_EN%22%3A%22Student%22%2C%22itaccounttype_TH%22%3A%22%E0%B8%99%E0%B8%B1%E0%B8%81%E0%B8%A8%E0%B8%B6%E0%B8%81%E0%B8%A9%E0%B8%B2%22%2C%22itaccounttype_id%22%3A%22StdAcc%22%2C%22lastname_EN%22%3A%22BOONMATA%22%2C%22lastname_TH%22%3A%22%E0%B8%9A%E0%B8%B8%E0%B8%8D%E0%B8%A1%E0%B8%B2%E0%B8%95%E0%B8%B2%22%2C%22organization_code%22%3A%221%22%2C%22organization_name_EN%22%3A%22Faculty+of+Humanities%22%2C%22organization_name_TH%22%3A%22%E0%B8%84%E0%B8%93%E0%B8%B0%E0%B8%A1%E0%B8%99%E0%B8%B8%E0%B8%A9%E0%B8%A2%E0%B8%A8%E0%B8%B2%E0%B8%AA%E0%B8%95%E0%B8%A3%E0%B9%8C%22%2C%22picture%22%3A%22https%3A%2F%2Fapp.scmc.cmu.ac.th%2Fapi%2Fuser%2F88546%2Fpicture%3Ftoken%3DLhGI15gaH0D55F%22%2C%22prename_EN%22%3A%22%22%2C%22prename_TH%22%3A%22%22%2C%22prename_id%22%3A%22OTH%22%2C%22sex_id%22%3A%221%22%2C%22student_id%22%3A%22670110278%22%7D; state=User; _ga_GYXSR60XKK=GS2.1.s1782284149$o3$g1$t1782284400$j60$l0$h0; _ga=GA1.1.628649458.1782273878',
        'Connection': 'keep-alive',
    }

    params = {
        'cmuitaccount': 'rattanon_boonmata@cmu.ac.th',
    }

    response = requests.get(
        'https://datagateway.library.cmu.ac.th/api/movie-streaming/claim/my',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    
def RetriveNetflix():

    cookies = {
        '_ga_GYXSR60XKK': 'GS2.1.s1782284149$o3$g1$t1782284403$j57$l0$h0',
        'entra_data': '%7B%22cmuitaccount%22%3A%22rattanon_boonmata%40cmu.ac.th%22%2C%22cmuitaccount_name%22%3A%22rattanon_boonmata%22%2C%22firstname_EN%22%3A%22RATTANON%22%2C%22firstname_TH%22%3A%22%E0%B8%A3%E0%B8%B1%E0%B8%90%E0%B8%99%E0%B8%99%E0%B8%97%E0%B9%8C%22%2C%22is_cmu%22%3Atrue%2C%22itaccounttype_EN%22%3A%22Student%22%2C%22itaccounttype_TH%22%3A%22%E0%B8%99%E0%B8%B1%E0%B8%81%E0%B8%A8%E0%B8%B6%E0%B8%81%E0%B8%A9%E0%B8%B2%22%2C%22itaccounttype_id%22%3A%22StdAcc%22%2C%22lastname_EN%22%3A%22BOONMATA%22%2C%22lastname_TH%22%3A%22%E0%B8%9A%E0%B8%B8%E0%B8%8D%E0%B8%A1%E0%B8%B2%E0%B8%95%E0%B8%B2%22%2C%22organization_code%22%3A%221%22%2C%22organization_name_EN%22%3A%22Faculty+of+Humanities%22%2C%22organization_name_TH%22%3A%22%E0%B8%84%E0%B8%93%E0%B8%B0%E0%B8%A1%E0%B8%99%E0%B8%B8%E0%B8%A9%E0%B8%A2%E0%B8%A8%E0%B8%B2%E0%B8%AA%E0%B8%95%E0%B8%A3%E0%B9%8C%22%2C%22picture%22%3A%22https%3A%2F%2Fapp.scmc.cmu.ac.th%2Fapi%2Fuser%2F88546%2Fpicture%3Ftoken%3DLhGI15gaH0D55F%22%2C%22prename_EN%22%3A%22%22%2C%22prename_TH%22%3A%22%22%2C%22prename_id%22%3A%22OTH%22%2C%22sex_id%22%3A%221%22%2C%22student_id%22%3A%22670110278%22%7D',
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
        # 'Cookie': '_ga_GYXSR60XKK=GS2.1.s1782284149$o3$g1$t1782284403$j57$l0$h0; entra_data=%7B%22cmuitaccount%22%3A%22rattanon_boonmata%40cmu.ac.th%22%2C%22cmuitaccount_name%22%3A%22rattanon_boonmata%22%2C%22firstname_EN%22%3A%22RATTANON%22%2C%22firstname_TH%22%3A%22%E0%B8%A3%E0%B8%B1%E0%B8%90%E0%B8%99%E0%B8%99%E0%B8%97%E0%B9%8C%22%2C%22is_cmu%22%3Atrue%2C%22itaccounttype_EN%22%3A%22Student%22%2C%22itaccounttype_TH%22%3A%22%E0%B8%99%E0%B8%B1%E0%B8%81%E0%B8%A8%E0%B8%B6%E0%B8%81%E0%B8%A9%E0%B8%B2%22%2C%22itaccounttype_id%22%3A%22StdAcc%22%2C%22lastname_EN%22%3A%22BOONMATA%22%2C%22lastname_TH%22%3A%22%E0%B8%9A%E0%B8%B8%E0%B8%8D%E0%B8%A1%E0%B8%B2%E0%B8%95%E0%B8%B2%22%2C%22organization_code%22%3A%221%22%2C%22organization_name_EN%22%3A%22Faculty+of+Humanities%22%2C%22organization_name_TH%22%3A%22%E0%B8%84%E0%B8%93%E0%B8%B0%E0%B8%A1%E0%B8%99%E0%B8%B8%E0%B8%A9%E0%B8%A2%E0%B8%A8%E0%B8%B2%E0%B8%AA%E0%B8%95%E0%B8%A3%E0%B9%8C%22%2C%22picture%22%3A%22https%3A%2F%2Fapp.scmc.cmu.ac.th%2Fapi%2Fuser%2F88546%2Fpicture%3Ftoken%3DLhGI15gaH0D55F%22%2C%22prename_EN%22%3A%22%22%2C%22prename_TH%22%3A%22%22%2C%22prename_id%22%3A%22OTH%22%2C%22sex_id%22%3A%221%22%2C%22student_id%22%3A%22670110278%22%7D; state=User; _ga=GA1.1.628649458.1782273878',
        'Connection': 'keep-alive',
    }

    json_data = {
        'cmuitaccount': 'rattanon_boonmata@cmu.ac.th',
        'phone': '0956975152',
    }

    response = requests.post(
        'https://datagateway.library.cmu.ac.th/api/movie-streaming/claim',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )