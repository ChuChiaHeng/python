import pygame
import sys
def check_click(pos,x_start,y_start,x_end,y_end):
    x_match=pos[0]>x_start and pos[0]<x_end
    y_match=pos[1]>y_start and pos[1]<y_end
    if x_match and y_match:
        return True
    else:
        return False
pygame.init()
WHITE=(255,255,255)
Black=(0,0,0)
width=700
height=500
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption('曾宥誠')
bg=pygame.Surface((width,height))
bg.fill(WHITE)
font_addr=pygame.font.get_default_font()
font=pygame.font.Font(font_addr,36)
title=font.render('Start',True,Black)
tit_w=title.get_width()
tit_h=title.get_height()
act=False
while True:
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if check_click(pygame.mouse.get_pos(),0,0,tit_w,tit_h):
                if act==False:
                    act=True
                    title=font.render('Start',True,Black)
    if act==True:
        pygame.draw.circle(bg,(0,0,0),(200,100),30,0)
        pygame.draw.circle(bg,(255,255,255),(210,100),15,0)
        pygame.draw.circle(bg,(0,0,0),(400,100),30,0)
        pygame.draw.circle(bg,(255,255,255),(410,100),15,0)
        pygame.draw.polygon(bg,(255,255,255),[[300,110],[280,170],[320,170]],0)
        pygame.draw.circle(bg,(0,0,0),(290,170),7,0)
        pygame.draw.circle(bg,(0,0,0),(310,170),7,0)
        pygame.draw.ellipse(bg,(255,0,0),[130,160,60,35],10)
        pygame.draw.ellipse(bg,(255,0,0),[400,160,60,35],10)
        pygame.draw.ellipse(bg,(255,255,0),[270,20,60,35],5)
        pygame.draw.line(bg,(255,100,150),(280,220),(320,220),5)
        pygame.draw.circle(bg,(0,0,0),(300,150),200,5)
    else:
        screen.blit(title,(0,0))
    pygame.display.update()