import requests
import json
import urllib.parse
import string
import random
from faker import Faker
from os import system
from time import sleep
from datetime import datetime
from variables import logo, user_agents
from colorama import init, Style, Fore, Back

init()
fake = Faker()
servidor = ""
perfil = ""
status = "Loading..."
contfracao = 1

def write_data(name, username, email, password, created, cont):
	nom = "profile-" + str(perfil) + ".txt"
	while True:
		try:
			with open(nom, "a") as file:
				file.write("Name: " + name + "\n")
				file.write("Username: " + username + "\n")
				file.write("Email: " + email + "\n")
				file.write("Password: " + password + "\n")
				file.write("Create at: " + created + "\n\n")
				print(Fore.GREEN + "\n[*] File " + str(int(cont)) + "/" + str(int(contfracao)) + " being saved...\n" + Style.RESET_ALL)
				break
		except:
			print(Fore.RED + "\n[-] Error saving file!\n" + Style.RESET_ALL)


def generate_password():
	characters = string.ascii_letters + string.digits + "!@#$%&*()-+/"
	passwd = ""
	cont = 1
	while cont < 12:
		passwd = str(passwd) + str(random.choice(characters))
		cont += 1
	cont = 0
	return passwd

def informations(nome, username, email, password, created, qtd, cont):
	global contfracao
	contfracao = qtd / 3
	calc = (qtd - cont) / 3
	tseconds = calc * 900
	tminutes = tseconds / 60
	thours = tminutes / 60
	tdays = thours / 24
	tmonths = tdays / 30
	tyears = tmonths / 12
	system("cls")
	print(Fore.GREEN + logo + Style.RESET_ALL)
	print(Fore.CYAN + "SERVER: " + Style.RESET_ALL + servidor + "       " + Fore.CYAN + "PROFILE: " + Style.RESET_ALL + perfil + "       " + Fore.CYAN + "DELAY: " + Style.RESET_ALL + "15m" + "       " + Fore.CYAN + "PACKAGES: " + Style.RESET_ALL + str(int(cont) + 1) + "       " + Fore.CYAN + "STATUS: " + Style.RESET_ALL + status + "\n")
	print(Fore.CYAN + "                                   ------> Meta: " + Style.RESET_ALL + str(qtd) + "       " + Fore.CYAN + "Left: " + Style.RESET_ALL + str(qtd - cont) + Fore.CYAN + " <------")
	print(Fore.CYAN + "[*] Name: " + Style.RESET_ALL + nome)
	print(Fore.CYAN + "[*] Username: " + Style.RESET_ALL + username)
	print(Fore.CYAN + "[*] Email: " + Style.RESET_ALL + email)
	print(Fore.CYAN + "[*] Password: " + Style.RESET_ALL + password)
	print(Fore.CYAN + "[*] Create at: " + Style.RESET_ALL + created + "\n")
	if tseconds > 60:
		if tminutes > 60:
			if thours > 24:
				if tdays > 30:
					if tmonths > 12:
						print(Fore.CYAN + "Restam: " + Style.RESET_ALL + str(tyears).replace(".", ",") + " years\n")
					else:
						print(Fore.CYAN + "Restam: " + Style.RESET_ALL + str(tmonths).replace(".", ",") + " months\n")
				else:
					print(Fore.CYAN + "Restam: " + Style.RESET_ALL + str(tdays).replace(".", ",") + " days\n")
			else:
				print(Fore.CYAN + "Restam: " + Style.RESET_ALL + str(thours).replace(".", ",") + " hours\n")
		else:
			print(Fore.CYAN + "Restam: " + Style.RESET_ALL + str(tminutes).replace(".", ",") + " minutes\n")
	else:
		print(Fore.CYAN + "Restam: " + Style.RESET_ALL + str(tseconds).replace(".", ",") + " seconds\n")

def generate_account(server, profile, qtd):
	cont = 0
	cont2 = 0
	cont3 = 1
	while cont < qtd:
		while cont2 < 3:
			nome = fake.name()
			username = nome.lower().replace(" ", "").replace(".", "")
			email = username + "@gmail.com"
			password = generate_password()
			url1 = None
			header_d6_earn_buzz =  {
				"Host": "d6-earn.buzz",
				"Cookie": "loclang=en; inviteclick=1; pid=" + profile[:-1] + "; parea=6; godomain=d6-earn.buzz; area=6; dldomain=d6-earn.buzz; pareaid=6; sidenav-state=pinned",
				"User-Agent": user_agents[random.randint(0, 71)],
				"Accept": "*/*",
				"Accept-Language": "en-US,en;q=0.5",
				"Accept-Encoding": "gzip, deflate",
				"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
				"X-Requested-With": "XMLHttpRequest",
				"Content-Length": "117",
				"Origin": "https://d6-earn.buzz",
				"Referer": "https://d6-earn.buzz/register.php",
				"Sec-Fetch-Dest": "empty",
				"Sec-Fetch-Mode": "cors",
				"Sec-Fetch-Site": "same-origin",
				"Te": "trailers"
			}
			header_u3a_earn_buzz =  {
				"Host": "a3-earn.buzz",
				"Cookie": "loclang=en; pid=" + profile[:-1] + "; dldomain=u3a-earn.buzz; pareaid=6; sidenav-state=pinned",
				"User-Agent": user_agents[random.randint(0, 71)],
				"Accept": "*/*",
				"Accept-Language": "en-US,en;q=0.5",
				"Accept-Encoding": "gzip, deflate",
				"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
				"X-Requested-With": "XMLHttpRequest",
				"Content-Length": "117",
				"Origin": "https://a3-earn.buzz",
				"Referer": "https://a3-earn.buzz/register.php",
				"Sec-Fetch-Dest": "empty",
				"Sec-Fetch-Mode": "cors",
				"Sec-Fetch-Site": "same-origin",
				"Te": "trailers"
			}
			data = "fullname=" + nome.replace(" ", "+") + "&username=" + username + "&email=" + username + "%40gmail.com&password=" + urllib.parse.quote(password)
			requisicao = None
			if server == "d6-earn.buzz":
				url1 = "https://" + server + "/api.php?act=register"
				try:
					requisicao = requests.post(url1, headers=header_d6_earn_buzz, data=data)
				except Exception as e:
					print(e)
			
			url1 = "https://a3-earn.buzz/api.php?act=register"
			try:
				requisicao = requests.post(url1, headers=header_u3a_earn_buzz, data=data)
			except Exception as e:
				print(e)
			responsejson = json.loads(requisicao.text)

			if responsejson["code"] == "1" and responsejson["message"] == "ok":
				created = str(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
				informations(nome, username, email, password, created, qtd, cont)
				write_data(nome, username, email, password, created, cont3)
				cont += 1
				cont2 += 1
			else:
				print("[-] Failed!")
		cont2 = 0
		cont3 += 1
		sleep(900)
	global status
	status = Fore.WHITE + Back.GREEN + Style.BRIGHT + " FINISHED " + Style.RESET_ALL
	informations("", "", "", "", "", qtd, qtd)
	print(Fore.GREEN + "\n[+] File '" + "profiles-" + str(perfil) + ".txt" + "' saved successfully!\n" + Style.RESET_ALL)
	system("pause")
		

def separator(url):
	global servidor, perfil
	if url[8:21][-1] == "/":
		servidor = url[8:20]
		perfil = url[21:]
	else:
		servidor = url[8:21]
		perfil = url[22:]

def fakeaccount():
	url = input("Enter your URL: ")
	qtd = input("Enter account number: ")
	if "https://" in url and "-earn.buzz/" in url:
		if qtd.isdigit():
			separator(url)
			generate_account(servidor, perfil, int(qtd))
