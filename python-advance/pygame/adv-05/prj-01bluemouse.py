import pygame
import random
import sys
import os
os.chdir(sys.path[0])
from pygame.locals import *
def check_click(pos1,x_start,y_start,x_end,y_end):
    x_match=pos1[0]>x_start and pos1[0]<x_end
    y_match=pos1[1]>y_start and pos1[1]<y_end
    if x_match and y_match:
        return True
    else:
        return False
WHITE=(255,255,255)
Black=(0,0,0)
orange=(255,100,0)
pygame.init()
bg_img="Gophers_BG_800x600.png"
bg=pygame.image.load(bg_img)

bg_x=bg.get_width()
bg_y=bg.get_height()
gopher=pygame.image.load('Gophers150.png')
a=0
screen=pygame.display.set_mode([bg_x, bg_y])
pygame.display.set_caption('曾宥誠')
sur=pygame.Surface([bg_x,bg_y])
pos6=[[610,440],[190,440],[400,440],[190,300],[610,300],[400,300]]
tick=0
max_tick=20
pos=pos6[0]
clock=pygame.time.Clock()
font_addr=pygame.font.get_default_font()
font=pygame.font.Font(font_addr,36)
title=font.render(str(a),True,orange)
tit_w=title.get_width()
tit_h=title.get_height()
pygame.mouse.set_visible(False)
mpos=(0,0)
while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if check_click(pygame.mouse.get_pos(),pos[0]-50,pos[1]-50,pos[0]+50,pos[1]+50):
                a+=1
                title=font.render(str(a),True,orange)
        elif event.type==MOUSEMOTION:
            mpos=pygame.mouse.get_pos()

    if tick>max_tick:
        new_pos=random.randint(0,5)
        pos=pos6[new_pos]
        tick=0
        
    else:
        tick=tick+1

    sur.blit(bg,(0,0))
    sur.blit(gopher, (pos[0]-gopher.get_width()/2,pos[1]-gopher.get_height()/2))
    pygame.draw.circle(sur,orange,mpos,10)
    screen.blit(sur, (0,0))
    screen.blit(title, (0,0))
    pygame.display.flip()