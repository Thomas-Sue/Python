# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 14:34:59 2017

@author: hp
"""

#CrowTaobaoPrice.py
import requests
import re
 
def getHTMLText(url):  #从url中获取r.text <html>
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    
def parsePage(ilt, html):   #解析html，提取价格和名称，返回列表
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])#提取列表中价格字符串，去引号            
            title = eval(tlt[i].split(':')[1])#提取列表中名称字符串，去引号
            ilt.append([price , title]) #列表类型,其元素为列表['9699.00', '国行ThinkPad T460S']
      
    except:
        print("")
 
def printGoodsList(ilt):       #格式化打印     
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))
         
def main():     #主函数
    goods = '联想T460s'
    depth = 3       #爬取深度，3页
    start_url = 'https://s.taobao.com/search?q=' + goods #搜索
    infoList = []  #ilt实参化
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i) #每页有44个商品
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
    
main()
 
            
            
            
            
            
            
            
            
            
            