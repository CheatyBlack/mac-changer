#!usr/bin/env/python

import os
import time

os.system("clear")
print("UPATING")
time.sleep(2)
os.system("sudo apt-get update")
time.sleep(2)
print("INSTALLING PYTHON3 AND PIP")
time.sleep(2)
os.system("sudo apt-get install python3-pip")
time.sleep(2)
print("INSTALLING PYTHON MODULES AND DEPENDENCIES")
time.sleep(2)
os.system("pip3 install lolcat")
time.sleep(2)
os.system("sudo apt-get install figlet")
time.sleep(2)
os.system("figlet COMPLTED | lolcat")
time.sleep(2)
print("done installing all dependencies")
print("run python3 mac_changer.py")
