# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-15 21:21:49
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-15 21:59:36
import requests
import sys
from bs4 import BeautifulSoup

def get_word_audio(word):
    url = f'https://ssl.gstatic.com/dictionary/static/sounds/oxford/{word}--_us_1.mp3'
    download = requests.get(url)
    if download.status_code == 200:
        with open(f'/Users/davidhansonc/Desktop/{word}.mp3', 'wb') as f: 
            f.write(download.content)
    else:
        print(f"Download Failed For File {word}.mp3")

get_word_audio(sys.argv[1])
