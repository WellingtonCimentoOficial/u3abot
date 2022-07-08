import requests
from time import sleep
from os import system
from colorama import init, Fore, Style, Back
from random import randint
from variables import logo, user_agents

init()
url = "https://"
value = 0
dalay = 0
servidor = "server"
perfil = "profile"
recived = 0
status = "Loading..."
pacotes = 1

def verifications():
  global url, value, dalay, servidor, perfil
  url1 = input("Enter your URL: ")
  if "https://" in url1 and "-earn.buzz/" in url1:
    value1 = input("Enter an amount ($USD): ")
    if value1.isnumeric():
      dalay1 = input("Enter the delay: ")
      if dalay1.isnumeric():
        url = url1
        value = value1
        dalay = dalay1
        if url1[8:21][-1:] == "/":
          servidor = url1[8:20]
          perfil = url1[21:]
        else:
          servidor = url1[8:21]
          perfil = url1[22:]
        princ()
      else:
        print("Invalid delay!")
        system("pause")
    else:
      print("Invalid value!")
      system("pause")
  else:
    print("Invalid url!")
    system("pause")


def secondqtd():
  return int(value) / 2 # quantas vezes o loop vai rodar

def timeleft(recived):
  DpM = (int(60 / int(dalay))) * 2 # dolares por minuto
  demoraS = (int(value) - recived) * int(dalay)
  demoraM = demoraS / 60
  demoraH = demoraM / 60
  demoraD = demoraH / 24
  demoraMes = demoraD / 30
  if int(demoraS) >= 60:
    if int(demoraM) >= 60:
      if int(demoraH) >= 24:
        if int(demoraD) >= 30:
          if int(demoraMes) >= 12:
            return str(demoraMes / 12).replace(".", ",") + " years"
          else:
            return str(demoraMes).replace(".", ",") + " months"
        else:
          return str(demoraD).replace(".", ",") + " days"
      else:
        return str(demoraH).replace(".", ",") + " hours"
    else:
      return str(demoraM).replace(".", ",") + " minutes"
  else:
    return str(demoraS).replace(".", ",") + " seconds"

def things(pacote):
  system("cls")
  print(Fore.GREEN + logo + Style.RESET_ALL)
  print(Fore.MAGENTA + "SERVER: " + Style.RESET_ALL + servidor + "       " + Fore.MAGENTA + "PROFILE: " + Style.RESET_ALL + perfil + "       " + Fore.MAGENTA + "DELAY: " + Style.RESET_ALL + str(int(dalay)) + "s" + "       " + Fore.MAGENTA + "PACKAGES: " + Style.RESET_ALL + str(pacote) + "       " + Fore.MAGENTA + "STATUS: " + Style.RESET_ALL + status + "\n")
  print(Fore.YELLOW + "[*] " + Style.RESET_ALL + "META: $" + value + " USD")
  print(Fore.GREEN + "[+] " + Style.RESET_ALL + "ATUAL: $" +  str(recived) + " USD")
  print(Fore.RED + "[-] " + Style.RESET_ALL + "FALTAM: $" + str(int(value) - recived) + " USD")
  print("\nTempo restante: " + timeleft(recived) + "\n\n")

def princ():
  for pacote in range(int(secondqtd())):
    try:
      agent = {"User-Agent": user_agents[randint(0,71)]}
      response = requests.get(url, headers=agent)
      pacotes =+ pacote
      if response.status_code == 200:
          global recived
          recived += 2
          things(pacotes)
    except Exception as e:
      #print(e)
      pass

    finally:
      sleep(int(dalay))
  global status
  status = Fore.WHITE + Back.GREEN + Style.BRIGHT + " FINISHED " + Style.RESET_ALL
  things(pacotes)
  system("pause")

def run():
  verifications()
