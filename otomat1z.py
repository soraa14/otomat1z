#!/usr/bin/python

import os
import sys
import time

# Pause Function
def pause():
    time.sleep(1)

# Nmap
pause()
print('## Running Nmap ###')
pause()
os.system('nmap -sC -sV DOMAIN')

# Whatweb
pause()
print('### Running Whatweb ###')
pause()
os.system('whatweb https://DOMAIN')

# Wafw00f
pause()
print('### Running Wafw00f ###')
pause()
os.system('wafw00f https://DOMAIN')

# Testssl
pause()
print('### Running Testssl ###')
pause()
os.system('testssl https://DOMAIN')

# Gobuster
pause()
print('### Running Gobuster ###')
pause()
os.system('gobuster dir -u https://DOMAIN -w /usr/share/seclist/Discovery/Web-Content/big.txt -x TBD')
