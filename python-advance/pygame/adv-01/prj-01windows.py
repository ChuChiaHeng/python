import pygame
import sys
pygame.init()
width=700
height=500
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("曾宥誠")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()