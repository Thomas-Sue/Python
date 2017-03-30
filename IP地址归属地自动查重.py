# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 20:54:12 2017

@author: hp
"""

import requests

url = 'http://m.ip138.com/ip.asp?ip='

try:
    r.requests.get(url+'202.204.80.112')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print r.text[-500:]
    
except:
    print "爬取失败"
