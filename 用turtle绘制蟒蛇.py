# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 16:59:13 2017

@author: hp
"""

import turtle
def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad,angle) #让小乌龟沿圆形爬行,半径-弧度值
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)  #向前直线爬行forward
    turtle.circle(neckrad+1, 180)
    turtle.fd(rad*2/3)
    
def main():
    turtle.setup(1300,800,0,0) #setup函数启动图形窗口,1300像素宽,800像素高
    pythonsize = 30
    turtle.pensize(pythonsize) #小乌龟运动轨迹宽度30像素
    turtle.pencolor('red') #小乌龟运动轨迹颜色
    turtle.seth(-40) #seth函数表示启动时运动方向(逆时针)
    drawSnake(40, 80 , 5 , pythonsize/2)
    
main()  