from earn import run
from fakeaccount import fakeaccount
from os import system
from time import sleep
from variables import logo
from colorama import init, Fore, Style

init()

def opc():
    system("cls")
    print(Fore.GREEN + logo + Style.RESET_ALL)
    print(Fore.GREEN + "                Version: " + Style.RESET_ALL + "1.0" + "                   " + Fore.GREEN + "Created: " + Style.RESET_ALL + "07-07-2022" + "                   " + Fore.GREEN + "Updated: " + Style.RESET_ALL + "07-07-2022\n")
    print("[1] - Make Money")
    print("[2] - Create fake accounts")
    print("[3] - Exit\n")

    op = int(input("Choose an option: "))
    return op

while True:
    op = opc()
    if op == 1:
        run()
        break
    elif op == 2:
        fakeaccount()
        break
    elif op == 3:
        exit()
    else:
        system("cls")
        print("Opção Inválida!\n")
        sleep(2)
