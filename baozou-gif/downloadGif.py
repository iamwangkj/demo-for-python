#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 爬取暴走漫画的gif图
import urllib.request
import bs4, os

page_sum = 2  #设置下载页数

path = os.getcwd()
print('path=', path)
path = os.path.join(path,'gif')
if not os.path.exists(path):
    os.mkdir(path)                                  #创建文件夹
url = "http://baozoumanhua.com/gif/month/page/"     #url地址
headers = {                                         #伪装浏览器
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                 ' Chrome/32.0.1700.76 Safari/537.36'
}
for count in range(page_sum):
    req = urllib.request.Request(
        url = url+str(count+1),
        headers = headers
    )
    print('请求路径=', req.full_url)
    content = urllib.request.urlopen(req).read()
    # print('内容=', content)
    soup = bs4.BeautifulSoup(content, features='lxml')                   # BeautifulSoup
    img_content = soup.findAll('img', attrs={'style':'width:460px'})
    url_list = [img['src'] for img in img_content]      #列表推导 url
    title_list = [img['alt'] for img in img_content]    #图片名称
    for i in range(url_list.__len__()) :
        imgurl = url_list[i]
        filename = path + os.sep +title_list[i] + '.gif'
        print(filename + ':' + imgurl)                         #打印下载信息
        urllib.request.urlretrieve(imgurl,filename)        #下载图片