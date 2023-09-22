
import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor
def main_apv():

    imt="110Y=="

    ak="ANONYMOUSPRO_200TAKA"

    os.system('clear')

    

    try:

        key1=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'r').read()
    except IOError:
        os.system("clear")
        print(logo)
        print ("\033[91;1m==+==+==+==+==+==+==+==+==+==+==+==+==+==+=\033[91;1m")
        print ("\033[92;1m==+==+==+==+==+==+==+==+==+==+==+==+==+==+==\033[92;1m")
        print ("\033[93;1mYOUR TOKEN IS NOT APROVAL\033[93;1m")     
        print ("\033[94;1m       YOUR TOKEN ⤵️🥰✅\033[94;1m")
        print ("\033[95;1m==+==+==+==+==+==+==+==+==+==+==+==+==+==+=\033[95;1m")
        print ("\033[96;1m==+==+==+==+==+==+==+==+==+==+==+==+==+==+=\033[96;1m")
        print ("")
        myid=uuid.uuid4().hex[:10].upper()
        print ("\033[96;1m          YOUR KEY : \033[96;1m"+ak+myid+imt)
        print ("\033[92;1m==+==+==+==+==+==+==+==+==+==+==+==+==+==+=\033[92;1m")
        print ("\033[93;1m==+==+==+==+==+==+==+==+==+==+==+==+==+==+=\033[93;1m")
        kok=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'w')
        kok.write(myid+imt)
        kok.close()
        print ("")
        print ("")
        print ("\033[91;1m==+==+==+==+==+==+==+==+==+==+==+==+==+==+=\033[91;1m")
        print ("\033[93;1m==+==+==+==+==+==+==+==+==+==+==+==+==+==+=\033[93;1m")
        print ("\033[92;1mCopy Key Sent WhatsApp Approvel Your Key \033[92;1m")
        print ("\033[94;1m==+==+==+==+==+==+==+==+==+==+==+==+==+==+=\033[94;1m")
        print ("\033[96;1m==+==+==+==+==+==+==+==+==+==+==+==+==+==+=\033[96;1m")
        time.sleep(3.5)
        tks = 'Dear%20Admin,%20Please%20Approved%20My%20Token%20To%20Premium%20% 20% 20%20%20My%20%20Key%20%20:%20'+ak+''+myid+''+imt

        os.system('am start https://wa.me/+15715652343?text=' + tks)

        

    r1=requests.get("https://github.com/anonymousproo/Clone-OLD-ids/blob/main/Approval.txt").text

    if key1 in r1:

        Main()

    else:

        os.system("clear")

        print (" \033[91;1m==+==+==+==+==+==+==+==+==+==+==+==+==+==+=\033[91;1m")
        print ("             \033[1;94mGIVE ME 200TAKA FOR APROVAL ANONYMOUSPRO\033[94;1m")     
           
        print ("             \033[1;32mYOUR KEY : "+ak+key1)     
        print ("\033[93;1m   Key And Sent Me WP Approvel Your Key \033[93;1m")
        print ("\033[92;1m==+==+==+==+==+==+==+==+==+==+==+==+==+==+=\033[92;1m")

        time.sleep(3.5)

        tks = 'Dear%20Admin,%20Please%20Apporved%20My%20Key%20To%20Premium✓✓%20%20%20%20%20My%20%20Key%20%20:%20'+ak+''+key1

        os.system('am start https://wa.me/+15715652343?text=' + tks)
        os.system("git clone https://github.com/anonymousproo/Clone-OLD-ids.git")
        

main_apv()
        