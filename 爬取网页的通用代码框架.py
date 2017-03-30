# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:02:44 2017

@author: hp
"""

import requests
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()   #若非200，则引发HTTPError
        r.encoding = r.appartent_encoding
        return r.text
    except:
        return "产生异常"
        
if __name__ == "__main__":
    url  = "http://www.icourse163.org"
    print(getHTMLText(url))

    