#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 爬取36氪的文章标题
import urllib3
from bs4 import BeautifulSoup


http = urllib3.PoolManager()
res = http.request('GET', 'https://36kr.com/')
# print(res.data)
content = res.data
soup = BeautifulSoup(content, features='lxml')
# 下面是完全匹配
# items = soup.find_all('p', attrs={'class': 'title-wrapper ellipsis-2'})
# 下面是局部匹配
items = soup.find_all('a', class_='article-item-title')

# print(items)
for child in items:
  print(child.string)
