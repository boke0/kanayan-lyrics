#!/usr/bin/python

from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
import requests

driver = Chrome()

i = 0
j = 0
while True:
    driver.get('https://www.joysound.com/web/search/artist/49968?startIndex='+str(i*20))

    soup = BeautifulSoup(driver.page_source.encode('utf-8'), 'html.parser')
    songlist = soup.select('#songlist>.jp-cmp-music-list-001>ul>li>div>a')
    if len(songlist) == 0:
        break
    for link in songlist:
        driver.get('https://www.joysound.com'+link['href'])

        soup = BeautifulSoup(driver.page_source.encode('utf-8'), 'html.parser')
        title_box = soup.select('#jp-cmp-main>.jp-cmp-box-001>header h1')[0]
        title = title_box.get_text().split('／')[0]
        song = soup.select('#lyrics .jspPane>p')
        print(title)
        with open('results/'+str(j)+'.txt', 'w') as f:
            f.write(title+'\n----\n')
            f.write(song[0].get_text())
        j+=1
    i+=1
