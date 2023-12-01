# -*- coding=utf-8 -*-
import pygame
import source.gamedata as gd
import source.country as country
import source.City as city

#全局变量之整个地图上城市数目（循环次数）
CITY_NUMBER = 17

BLACK = (0,0,0)
WHITE = (255,255,255)
LIGHTGRAY = (200,200,200)
GRAY = (100,100,100)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
PURPLE = (255,0,255)

#颜色列表
colorlist = [WHITE,BLUE,RED,BLACK,GREEN,PURPLE]

#联通路径表，第i个是城市i的所有联通城市
maproad = [
    [0],
    [2,4,8,10,11],
    [1,3,4,8],
    [2,5],
    [1,2,3,5,6,11],
    [3,4,6],
    [4,5,7,11],
    [6],
    [1,2,9],
    [8,10,13,14],
    [1,9,11,14,15,17],
    [1,4,6,10,12,15],
    [11,15,16],
    [9,14],
    [9,10,13,17],
    [10,11,12,16,17],
    [12,15],
    [10,14,15]
]
    

def draw_city(screen,country,x,y):
    '''绘制单一城市 20*20矩形带颜色方块'''
    xx=20*x
    yy=20*y+100
    pygame.draw.rect(screen, colorlist[country], (xx, yy, 20, 20),0)

def drawmap(screen):
    '''绘制全部城市，调用gamedata的城市列表信息'''
    i = 0
    while i < CITY_NUMBER:
        ct = int(gd.citylist[i].country)
        x = int(gd.citylist[i].cityx)
        y = int(gd.citylist[i].cityy)
        draw_city(screen,ct,x,y)
        i = i + 1

def mouseMoveMap(mx,my):
    '''判断全部城市的鼠标移动'''
    i = 0
    while i < CITY_NUMBER:
        gd.citylist[i].getFocus(mx,my)
        i = i + 1

def mouseDownMap(mx,my):
    '''判断全部城市的鼠标点击'''
    i = 0
    while i < CITY_NUMBER:
        gd.citylist[i].mouseDown(mx,my)
        i = i + 1

def mouseUpMap():
    i = 0
    while i < CITY_NUMBER:
        gd.citylist[i].mouseUp()
        i = i + 1

def isadj(city1,city2):
    '''判断城市1和城市2是否联通'''
    x = int(city1)
    y = maproad[x]
    if ( city2 in y ):
        return True
    else:
        return False


