# -*- coding=utf-8 -*-
import pygame

class Window:
    ''' 游戏子窗口类，在界面上绘制 '''
    def __init__(self,x,y,l,h,color):
        self.x = x
        self.y = u
        self.l = l
        self.h = h
        self.color = color

    def draw(self,screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.l, self.h),0)

    
