# -*- coding=utf-8 -*-
import random
import pygame
import source.gamedata as gd
import source.country as country
import source.Map as Map
import source.Button as Btn
import source.Window as window
pygame.init()
screencaption = pygame.display.set_caption('城市战争')
screen = pygame.display.set_mode((1200,750))
backmap = pygame.image.load("backmap.png").convert()

# 颜色列表
BLACK = (0,0,0)
WHITE = (255,255,255)
LIGHTGRAY = (200,200,200)
GRAY = (100,100,100)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
PURPLE = (255,0,255)

colorlist = [WHITE,BLUE,RED,BLACK,GREEN,PURPLE]

# 字体相关
font = pygame.font.SysFont("SimHei", 48)
nianhao = '天和'
year = 1

# 绘制ui
def drawui():
    pygame.draw.rect(screen, BLACK, (0, 0, 1200, 100),0)
    pygame.draw.rect(screen, LIGHTGRAY, (800, 100, 400, 700),0)
    screen.blit(backmap,(0,100))

# 按钮测试，待删
def buttontest():
    print('aaaaaa')
    global year
    year = year - 1

btn1 = Btn.Button(900,20,100,60,'测试',RED,buttontest,WHITE,24)

while True:
    mx,my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                year = year + 1
        if event.type == pygame.MOUSEMOTION:
            btn1.getFocus(mx,my)
            Map.mouseMoveMap(mx,my)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == ( 1, 0, 0 ):
                btn1.mouseDown(mx,my)
                Map.mouseDownMap(mx,my)
        if event.type == pygame.MOUSEBUTTONUP:
            btn1.mouseUp()
            Map.mouseUpMap()

    screen.fill(WHITE)
    
    drawui()
    Map.drawmap(screen)
    btn1.draw(screen)
    
    # 年号显示逻辑
    currentstring = nianhao + str(year) + '年'
    textNianhao = font.render(currentstring, True, WHITE)
    screen.blit(textNianhao, (10,10))
    
    pygame.display.update()
