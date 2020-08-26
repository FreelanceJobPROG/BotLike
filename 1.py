# -*- coding: utf-8 -*-
import sqlite3
import logger
import os
from instagram_private_api import Client, ClientCompatPatch
from instagram_private_api import constants
import requests
import json
# ------------------------------------------------------------------
# # ОБЪЯВЛЕНИЕ ПЕРЕМЕННЫХ
# ------------------------------------------------------------------

BASE_URL = 'https://www.instagram.com/'
LOGIN_URL = BASE_URL + 'accounts/login/ajax/'

session = requests.Session()
session.headers = {
	'User-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 Instagram 63.0.0.14.94 (iPhone9,3; iOS 11_4_1; ru_RU; ru-RU; scale=2.00; gamut=wide; 750x1334)',
}
session.headers.update({'Referer': BASE_URL})
user_name = 'Логин'
password = 'Пароль'
constants.Constants.PHONE_MODEL = 'HUAWEI'
constants.Constants.APP_VERSION = '80.0.3987.99'
constants.Constants.ANDROID_VERSION = 7

# ------------------------------------------------------------------
# # ВХОД
# ------------------------------------------------------------------
req = session.get(BASE_URL)
session.headers.update({'X-CSRFToken': req.cookies['csrftoken']})
login_data = {'username': user_name, 'password': password}

#Finally login in
login = session.post(LOGIN_URL, data=login_data, allow_redirects=True)
session.headers.update({'X-CSRFToken': login.cookies['csrftoken']})

cookies = login.cookies

#Print the html results after I've logged in
print(login.text)
#-------------------------------------------------------------------
if os.path.exists('inst.db'):
	print ('Запуск цикла')
else:
	conn = sqlite3.connect("inst.db") # или :memory: чтобы сохранить в RAM
	cursor = conn.cursor()
 	# Создание таблицы
	cursor.execute("""CREATE TABLE ID (ID text,FLAG text)""")
	Login = open('Login.txt')
	for line in Login.readlines():
			line = line.replace("\n", "")
			link='https://www.instagram.com/'
			flag='?__a=1'
			url = link+line+flag
			response = session.get(url)
			data = json.loads(response.text)
			id=data['graphql']['user']['id']
			LoginID = open("ID.txt", "a")
			LoginID.write(id+"\n")
	LoginID.close()
	Login.close()
	os.remove('Login.txt')
	FID = open('ID.txt')
	for lid in FID.readlines():
		lid = line.replace("\n", "")
		cursor.execute("""INSERT INTO  ID VALUES ('"""+lid+"""', 0)""")
	FID.close()
	os.remove('ID.txt')

