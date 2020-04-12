

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.sina.com.cn/china/')

res.encoding = "utf-8"
soup = BeautifulSoup(res.text,'html.parser')
#print(soup)
for news in soup.select('.right-content'):
    if len(news.select('ul')) > 0:
        h2 = news.select('li')[0].text
        #time = news.select('.feed-card-time')[0].text
        a = news.select('a')[0]['href']
        print(h2,a)


