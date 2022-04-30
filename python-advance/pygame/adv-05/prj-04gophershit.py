import pygame
import random
import sys
import os
import time
os.chdir(sys.path[0])
from pygame.locals import *

times=0
tmax=20   

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
a=0
screen=pygame.display.set_mode([bg_x, bg_y])
sur=pygame.Surface([bg_x,bg_y])
pos6=[[610,440],[190,440],[400,440],[190,300],[610,300],[400,300]]
tick=0
max_tick=20
pos=pos6[0]
clock=pygame.time.Clock()

typeface=pygame.font.get_default_font()
font=pygame.font.Font(typeface,36)
title=font.render(str(a),True,orange)

end_font=pygame.font.Font(typeface,36)
end_sur=end_font.render(str(times),True,WHITE)

ham1=pygame.image.load("Hammer1.png")
ham2=pygame.image.load("Hammer2.png")
gopher=pygame.image.load('Gophers150.png')
gophers2=pygame.image.load("Gophers2_150.png")
pygame.mixer.music.load("hit.mp3")

pygame.mouse.set_visible(False)
mpos=(0,0)

while True:
    clock.tick(30)
    hammer=ham2
    hitsur=gopher
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mpos=pygame.mouse.get_pos()
            hammer=ham1
            if check_click(pygame.mouse.get_pos(),pos[0]-50,pos[1]-50,pos[0]+50,pos[1]+50):
                if times<tmax:
                    tick=max_tick+1
                    pygame.mixer.music.play()
                    a+=1
                    hitsur=gophers2
                    title=font.render(str(a),True,orange)
        elif event.type==MOUSEMOTION:
            mpos=pygame.mouse.get_pos()
    if times > tmax :
        sur.fill((0,0,0))
        pygame.mouse.set_visible(True)
        end_sur=font.render("Your Score is:{}/{}".format(a,tmax),True,orange)
        screen.blit(sur,(0,0))
        screen.blit(end_sur,(100,100))
        pygame.display.flip()
    else:
        if tick>max_tick:
            times+=1
            score_sur=font.render(str(a),True,WHITE)
            end_sur=font.render(str(times),True,WHITE)
            new_pos=random.randint(0,5)
            pos=pos6[new_pos]
            tick=0
            
        else:
            tick=tick+1

        sur.blit(bg,(0,0))
        sur.blit(hitsur, (pos[0]-hitsur.get_width()/2,pos[1]-hitsur.get_height()/2))
        sur.blit(hammer,(mpos[0]-hammer.get_width()/2,mpos[1]-hammer.get_height()/2))
        screen.blit(sur, (0,0))
        screen.blit(title, (0,0))
        screen.blit(end_sur,(bg_x-end_sur.get_width()-10,10))
        pygame.display.flip()
        if (hammer==ham1 or hitsur==gophers2):
            time.sleep(0.1)