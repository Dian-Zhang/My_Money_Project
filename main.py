import os
import sys

import requests
from bs4 import BeautifulSoup
import json
import time
import random
from you_get import common
from urllib.request import urlretrieve


def get_html_text(url):
    try:
        h = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                           'AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/68.0.3440.106 Safari/537.36'
             }
        r = requests.get(url, headers=h, timeout=3000)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print("异常:", e)
        return str(e)


def download_video(url, filename):
    my_video = urlretrieve(url=url, filename=filename)

#Expires
#ssig=A9v8k%2FGjLF
url = "https://f.video.weibocdn.com/o0/pJPWsp3Olx07Rl2uAQH601041205xymo0E020.mp4?label=mp4_1080p&template=1920x1080.25.0&trans_finger=d88af6227b88881484d2b59dfbafa136&media_id=4702789843222651&tp=8x8A3El:YTkl0eM8&us=0&ori=1&bf=3&ot=h&ps=3lckmu&uid=3ZoTIp&ab=3915-g1,1493-g0,1192-g0,1191-g0,1258-g0,3601-g15&Expires=1636987177&ssig=ucPzsd0inD&KID=unistore,video"
filename = "G:\\Code\\My_Money_Project\\Video\\test.mp4"
download_video(url, filename)
print("@@@@@@@@下载结束@@@@@@")
