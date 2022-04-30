#===載入套件開始
from time import time
import pygame 
import sys 
import os 
os.chdir(sys.path[0])
#***載入套件結束***


#===初始化設定開始===
pygame.init()
timer=0
clock=pygame.time.Clock()
#***初始化設定結束***


#===載入圖片開始===
img=pygame.image.load("image/bg.png")
#***載入圖片結束***


#===遊戲視窗設定開始===
bg_x=img.get_width()
bg_y=img.get_height()
bg_size=(bg_x,bg_y)
roll_x=0

pygame.display.set_caption("Dinosaur")
screen=pygame.display.set_mode(bg_size)
#***遊戲視窗設定結束***


#===分數設定開始===

#***分數設定結束***


#===恐龍設定開始===

#***恐龍設定結束***


#===仙人掌設定開始===

#***仙人掌設定結束***


#***碰撞設定開始***

#***碰撞設定結束***


#===GameOver設定開始===

#***GameOver設定結束***


#===主程式開始===
while True:
    #===計時與速度===
    clock.tick(100)
    timer+=1
    #===偵測鍵盤事件開始===
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    #===遊戲結束===       

    #===遊戲進行===        
    roll_x=(roll_x-10) % bg_x
    print(roll_x)
    print(roll_x-bg_x)
    screen.blit(img,[roll_x-bg_x,0])
    screen.blit(img,[roll_x,0])

    #===更新角色狀態===
    pygame.display.update()
#===主程式結束===