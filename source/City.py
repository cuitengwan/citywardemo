# -*- coding=utf-8 -*-
import random

class City:
    '''
        城市类
        包括：城市id，名称，归属国家，兵力，金钱，产能
        待增加：人口，粮食等内容
        交互方式是按钮
    '''
    NORMAL = 0
    MOVE = 1
    DOWN = 2
    def __init__(self,cityid,cityx,cityy,cityname,country,soldier,money,ic):
        self.status = City.NORMAL
        self.cityid = cityid
        self.cityx = cityx
        self.cityy = cityy
        self.cityname = cityname
        self.country = country
        self.soldier = soldier
        self.money = money
        self.ic = ic

    def city_basic(self):
        return self.cityid,self.cityname,self.country,self.soldier,self.money,self.ic

    def judge(self,x,y):
        # collide?
        xx = int(self.cityx) * 20
        yy = int(self.cityy) * 20 + 100
        xr = xx + 20
        yd = yy + 20
        if (xx<x<xr)&(yy<y<yd):
            return True
        else:
            return False

    def getFocus(self,x,y):
        # when the mouse move on button
        if self.status==City.DOWN:
            return
        if self.judge(x,y):
            self.status = City.MOVE
        else:
            self.status = City.NORMAL

    def mouseDown(self,x,y):
        # click the button
        # can have return value
        if self.judge(x,y):
            self.status = City.DOWN

    def mouseUp(self):
        if self.status==City.DOWN:
            self.status = City.NORMAL
            #return func
            print(self.cityid)
            return 0
    
    def zhengbing(self,bingli):
        '''征兵，每10000人花1块钱，不足的也要1块钱'''
        cost = bingli / 10000
        if cost > self.money:
            return 1
        else:
            self.money = self.money - cost
            self.soldier = self.soldier + bingli
            return 0
        
    def jiejia(self,bingli):
        '''裁军，暂时不花钱'''
        if bingli > self.soldier:
            return 1
        else:
            self.soldier = self.soldier - bingli
            return 0
        
    def jiaoshui(self,x):
        '''金钱从城市到中央'''
        if x > self.money:
            return 1
        else:
            self.money = self.money - x
            return 0
        
    def bokuan(self,x):
        '''金钱从中央到城市'''
        self.money = self.money + x

    def touzi(self):
        '''投资，花费5块钱，IC+1'''
        if self.money > 5:
            self.money = self.money - 5
            self.ic = self.ic + 1
            return 0
        else:
            return 1
        
    def chaichu(self):
        '''拆除，用1点IC随机获得1到10块钱'''
        if self.ic > 0:
            self.money = self.money + random.randint(1,10)
            self.ic = self.ic - 1
            return 0
        else:
            return 1


