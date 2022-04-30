import pygame
import sys
pygame.init()
WHITE=(255,255,255)
COLOR=(90,60,30)
width=640
height=320
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption('曾宥誠')
bg=pygame.Surface((width,height))
bg.fill(COLOR)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    screen.blit(bg,(0,0))
    pygame.display.update()