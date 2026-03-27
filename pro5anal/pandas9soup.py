# Beautiful Soup 객체를 이용한 웹 문서 처리

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import requests
from bs4 import BeautifulSoup

baseurl = "https://www.naver.com"
headers = {"User-Agent":"Mozilla/5.0"}

source = requests.get(baseurl, headers=headers)
print(source, type(source))
print(source.status_code)
# print(source.text, type(source.text))   # <class 'str'>
print(source.content)

conv_data = BeautifulSoup(source.text, 'lxml')
# print(conv_data, type(conv_data))   # 이제는 <class 'bs4.BeautifulSoup'>

for atag in conv_data.find_all('a'):
    href = atag.get('href')
    title = atag.get_text(strip = True)
    if title:
        print(href)
        print(title)
        print('--------')






