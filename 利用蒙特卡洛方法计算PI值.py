# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 17:50:45 2017

@author: hp
"""

'''蒙特卡洛方法计算Pi值'''

from random import random 
from math import sqrt
from time import clock

DARTS = 1200
hits = 0
clock()

for i in range(1,DARTS):
    x, y = random(), random()
    dist = sqrt(x**2 + y**2)
    if dist <= 1.0 :
        hits += 1
        
pi = 4 * (hits/DARTS)
print("pi 的值是 %s" %pi)
print("程序运行的时间是 %-5.5ss" % clock())
    