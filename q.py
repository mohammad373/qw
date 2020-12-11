# qw

# xmrlpc   xmrlpc.php

import os
import sys
import requests
import time
from colorama import Fore

my_list = ["xmlrpc.php" , "xmlrpc" , "xmrlpc" , "xmrlpc.php"]

def __1__():
    os.system("clear")
    time.sleep(1)
    print(Fore.YELLOW + "Hello . Welcome ;)")
    time.sleep(1)
    target = input(Fore.GREEN + "Pleass Enter The Address Target ==>  ")
    if target == "" or None :
        try:
            time.sleep(1)
            print(Fore.RED + "Error : Your Target Is Not Found ;(")
            time.sleep(1)
            sys.exit()
        except:
            pass
    r = target + "/" + "wp-content/plugins/"
    r2 = requests.get(r)
    if r2.status_code == 404 or r2.status_code == 500:
        time.sleep(1)
        print(Fpre.RED + "Your Target Is Not wordPress ;(")
        time.sleep(1)
        sys.exit()
    else:
        time.sleep(1)
        print(Fore.GREEN + "Your Target Is WordPress ;)")
        time.sleep(1)
        for i in my_list:
            q = target + "/" + "wp-content/plugins/" + i
            if q.status_code == 200:
                print(Fore.GREEN + q)
            else:
                print(Fore.RED + q)
__1__()
