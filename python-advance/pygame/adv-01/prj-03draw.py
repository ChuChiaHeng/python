import pygame
import sys
pygame.init()
WHITE=(255,200,100)
width=700
height=500
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption('曾宥誠')
bg=pygame.Surface((width,height))
bg.fill(WHITE)
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
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    print(pygame.mouse.get_pos())
    screen.blit(bg,(0,0))
    pygame.display.update()