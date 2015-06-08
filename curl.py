#!/usr/bin/env python
#-*- coding: utf-8 -*-
#encoding=utf-8

import urllib2
import urllib
import os
from BeautifulSoup import BeautifulSoup

#当前页面的类型，如：iPhone6，iPhone6 plus，iPhone5，iPhone4，iPhone3，
def getAllPages(cPage):
    cUrl = 'http://ios.25pp.com/wallpaper/7_0_1_{cPage}/'
    cUrl = cUrl.format(cPage=cPage)
    return getAllImageLink(cUrl)

#获取当前页面的所以图片
def getAllImageLink(cpage):
    #iphone6-game
    html = urllib2.urlopen(cpage).read()
    soup = BeautifulSoup(html)

    liResult = soup.findAll('dl',attrs={"class":"wp_list"})

    for li in liResult:
        imageEntityArray = li.findAll('img')
        
        for image in imageEntityArray:
            link = image.get('src')
            
            imageName = image.get('alt')
            
            filesavepath = '/Users/jason/Desktop/curl/iphone6-game/%s.jpg' % imageName 
            urllib.urlretrieve(link,filesavepath)
            print filesavepath;

if __name__ == '__main__':
    num = 0
    for num in xrange(1,77):
        getAllPages(num)
#     getAllImageLink()
    
