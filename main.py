import datetime
import urllib
from bs4 import BeautifulSoup
import urllib.request as req
import requests
import json


now = datetime.datetime.now()
nowDate = now.strftime('%Y년 %m월 %d일 %H시 %M분 입니다.')

str += '   Current Datetime, ' + nowDate
str += '   오늘의 날씨 정보입니다.\n'
print('   Current Datetime, ' + nowDate)
print('   오늘의 날씨 정보입니다.\n')

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
title = soup.find("title").string
weather_info = soup.find("wf").string

str += title
str += weather_info.replace("<br />", "\n "), sep='\n'
print(title)
print(weather_info.replace("<br />", "\n "), sep='\n')

webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8')

soup = BeautifulSoup(webpage, 'html.parser')
temps = soup.find('div','temperature_text')
summary = soup.find('p','summary')
str += '\n'
str += "서울 " + temps.text.strip()
str += summary.text.strip()
print('\n')
print("서울 " + temps.text.strip())
print(summary.text.strip())

url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers={
    "Authorization" : "Bearer " + "M4KnKwDqY5DN3JK6nlckO6Tpyt3pl2xXV0_37AMBCj1zTgAAAYmrUEFe"
}

data = {
       'object_type': 'text',
       'text': str,
       'link': {
           'web_url': 'https://weather.naver.com/today/09680640?cpName=KMA',
           'mobile_web_url': 'https://weather.naver.com/today/09680640?cpName=KMA'
       },
       'button_title': '날씨보기'
   }

data = {'template_object': json.dumps(data)}
response = requests.post(url, headers=headers, data=data)
response.status_code
