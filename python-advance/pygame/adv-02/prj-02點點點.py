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
width=640
height=400
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption('曾宥誠')
bg_img="pygame/adv-02/snow.jpg"
bg=pygame.image.load(bg_img)
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
                elif act==True:
                    act=False
                    title=font.render('Stop',True,Black)
    screen.blit(title,(0,0))
    pygame.display.update()