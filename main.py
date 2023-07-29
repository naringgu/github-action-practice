import datetime
import urllib
from bs4 import BeautifulSoup
import urllib.request as req

now = datetime.datetime.now()
nowDate = now.strftime('%Y년 %m월 %d일 %H시 %M분 입니다.')

print("\n   Python Weather Crawling 2022 Revise\n ")
print('   Current Datetime, ' + nowDate)
print('   오늘의 날씨 정보입니다.\n')

# 기상청에서 데이터를 가져옵니다.
url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
res = req.urlopen(url)
# res = req.urlopen("http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp")
soup = BeautifulSoup(res, "html.parser")
# Html 수프를 떠요. 우리가 지정해준 url을 파이썬이 대신 열어서 해당 html 파일을 파싱 (복사)해옵니다.

title = soup.find("title").string
# html 구문 분석 결과 타이틀을 가져올거에요

weather_info = soup.find("wf").string
print(title)
print(weather_info)
# 좀더 깔끔하게 표현하려면 print 함수내에 내장된 sep 기능과 텍스트 치환기능 을 활용해요
# print(weather_info.replace("<br />","\n "),sep='\n')


#네이버 날씨 크롤링
# Phase1 Seoul Weather Crawling

webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8')

soup = BeautifulSoup(webpage, 'html.parser')
temps = soup.find('div','temperature_text')
summary = soup.find('p','summary')
# print(temps)
print("서울 "+temps.text.strip())
# print(summary)
print(summary.text.strip())