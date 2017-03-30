# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 10:36:20 2017

@author: hp
"""


import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = "utf-8"
        return r.text
    except:
        return ""


def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):            
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])

def printUnivList(ulist,num):
    print ("{:^10}\t{:^10}\t{:^10}".format("排名","学校名称","总分"))
    for i in range(num):
        u = ulist[i]
        print ("{:^10}\t{:^10}\t{:^10}".format(u[0],u[1],u[2]))


#主函数main（）
def  main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)        #univs 20
main()
    
    
    
    
    
    
    
    
    
    
    
    
    
