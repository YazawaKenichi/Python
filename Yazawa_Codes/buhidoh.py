import requests
from bs4 import BeautifulSoup
import re
import os
import pprint
import time
import urllib.error
import urllib.request

def download_file(imageurl, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode = 'wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)

URLFILEPATH = 'url'
LOGFILEPATH = 'log'

with open(URLFILEPATH, mode = 'rt', encoding = 'utf-8') as urllist:
    with open(LOGFILEPATH, mode = 'at', encoding = 'utf-8') as loglist:
        url = urllist.readline()    # 改行コードも含めて一行取得する

        while url:
            # print(url.strip())  # 余計な文字を削除する。具体的には改行を削除する。
            loglist.write(url)
            address = str(url.strip())
            # print(address)
            resp = requests.get(address)
            print(str(resp))
            """
            data = response.text
            html = BeautifulSoup(data, 'lxml')
            ently_text = html.find_all(class_ = "ently_text")
            print(ently_text)
            page = 0
            for anchor in ently_text.a:
                page += 1
                print(str(anchor['href']))
                download_file(str(anchor['href']), './' + page + '.jpg')
            """
            url = urllist.readline()

