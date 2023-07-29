import datetime
import urllib
from bs4 import BeautifulSoup
import urllib.request as req

now = datetime.datetime.now()
nowDate = now.strftime('%Y년 %m월 %d일 %H시 %M분 입니다.')

print("\n   Python Weather Crawling 2022 Revise\n ")
print('   Current Datetime, ' + nowDate)
print('   오늘의 날씨 정보입니다.\n')

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
title = soup.find("title").string
weather_info = soup.find("wf").string
print(title)
print(weather_info.replace("<br />", "\n "), sep='\n')

webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8')

soup = BeautifulSoup(webpage, 'html.parser')
temps = soup.find('div','temperature_text')
summary = soup.find('p','summary')

print("서울 " + temps.text.strip())
print(summary.text.strip())