# -*- coding=utf-8 -*-
import pygame
class Button:
    NORMAL = 0
    MOVE = 1
    DOWN = 2
    def __init__(self, x, y, l, h, text=' ', color=(100,0,0), func=None, fontcolor=(0,0,0) , fontsize=24 ):
        self.status = Button.NORMAL
        self.x = x
        self.y = y
        self.l = l
        self.h = h
        self.text = text
        self.color = color
        self.func = func
        #self.font = pygame.font.SysFont("SimHei", fontsize)
        #self.fontSurface = pygame.font.render(self.text, True, fontcolor)

    def draw(self,destSurf):
        # draw the button
        #dx = (self.l/2) - (self.fontSurface.get_width()/2)
        #dy = (self.h/2) - (self.fontSurface.get_height()/2)
        pygame.draw.rect(destSurf, (100,0,0) , (self.x, self.y, self.l, self.h), 0)
        #destSurf.blit(self.fontSurface, (self.x+dx,self.y+dy))


    def judge(self,x,y):
        # collide?
        xr = self.x + self.l
        yd = self.y + self.h
        if (self.x<x<xr)&(self.y<y<yd):
            return True
        else:
            return False
            
    def getFocus(self,x,y):
        # when the mouse move on button
        if self.status==Button.DOWN:
            return
        if self.judge(x,y):
            self.status = Button.MOVE
        else:
            self.status = Button.NORMAL

    def mouseDown(self,x,y):
        # click the button
        # can have return value
        if self.judge(x,y):
            self.status = Button.DOWN

    def mouseUp(self):
        if self.status==Button.DOWN:
            self.status = Button.NORMAL
            if self.func:
                return self.func()
