#!usr/bin/env/python

import subprocess
import time
import os
import lolcat

Y = set(['yes', 'y', 'YES', 'Y'])
N = set(['no', 'n', 'NO', 'N'])

interface = input("Enter Your Interface To Change Your Mac Address >> ")
new_mac = input("Enter Your New_Mac To Be Changed >> ")
alert = input("Are You Sure You Want To Change Your Mac Address Y / N ")

def scanner():
    if alert in Y:
        os.system("figlet CHANGING MAC | lolcat")
        time.sleep(2)
        os.system("clear")
        time.sleep(2)
        subprocess.call("ifconfig" + interface + "down", shell=True)
        subprocess.call("ifconfig" + interface + "hw" + "ether" + new_mac, shell=True)
        subprocess.call("ifconfig" + interface + "up", shell=True)
        os.system("figlet CHANGED | lolcat")
        time.sleep(2)
        print("SuccessFully Changed Your Mac Address To " + new_mac)
    elif alert in N:
        os.system("figlet OK BYE | lolcat")
        time.sleep(1)
        exit()
scanner()
