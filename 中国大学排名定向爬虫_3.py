# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 14:20:12 2017

@author: hp
"""

# coding=utf-8
import requests
from bs4 import BeautifulSoup
import bs4
import sys
reload(sys)
sys.setdefaultencoding('utf8')
 
def get_html(url):
    try:
        r = requests.get(url, timeout=300)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'get url error'
 
 
def save_rank(html, u_list):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.tbody.children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr.find_all('td')
            u_list.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])
 
 
def print_rank(u_list, num):
    p_format = "{0:^10}{1:{4}^12}{2:{4}^12}{3:^10}"
    print(p_format.format(u"排名", u"学校", u"省份", u"总分", unichr(12288)))
    for i in range(num):
        u = u_list[i]
        print(p_format.format(u[0], u[1], u[2], u[3], unichr(12288)))
 
 
def main():
    u_list = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    num = 20
    html = get_html(url)
    save_rank(html, u_list)
    print_rank(u_list, num)
 
 
main()