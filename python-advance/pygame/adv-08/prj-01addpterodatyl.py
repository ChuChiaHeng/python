#===載入套件開始
from time import time
import pygame
import sys
import os
import random

os.chdir(sys.path[0])
from pygame.locals import *
#***載入套件結束***

#===初始化設定開始===
LIMIT_LOW = 140
LIMIT_HIGH = 140
pygame.init()
timer = 0
clock = pygame.time.Clock()
RED = (255, 0, 0)
xxx = 0
#***初始化設定結束***

#===載入圖片開始===
img = pygame.image.load("image/bg.png")
img_dinosaur = [
    pygame.image.load("image/小恐龍1.png"),
    pygame.image.load("image/小恐龍2.png")
]
img_cacti = pygame.image.load("image/cacti.png")
img_ptera = [
    pygame.image.load('image/翼龍飛飛1.png'),
    pygame.image.load('image/翼龍飛飛2.png')
]
img_bend_down = [
    pygame.image.load("image/小恐龍蹲下1.png"),
    pygame.image.load("image/小恐龍蹲下2.png")
]
img_gg = pygame.image.load('image/gameover.png')
img_monster = pygame.image.load('image/teacher2.png')
#***載入圖片結束***

#===遊戲視窗設定開始===
bg_x = img.get_width()
bg_y = img.get_height()
bg_size = (bg_x, bg_y)
roll_x = 0

pygame.display.set_caption("Dinosaur")
screen = pygame.display.set_mode(bg_size)
#***遊戲視窗設定結束***

#===分數設定開始===
score = 0
got_score = False
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 36)
score_sur = score_font.render(str(score), False, RED)


def get_score(win):
    global score, score_sur
    score_sur = score_font.render(str(score), True, RED)
    win.blit(score_sur, [10, 10])


#***分數設定結束***

#===恐龍設定開始===
dino_show = img_dinosaur
dino_limit = LIMIT_LOW
ds_x = 50
ds_y = dino_limit
jumpState = False
jumpValue = 0


def get_dino_limit(dino_img):
    return bg_y - 100 - dino_img[0].get_height()


def move_dinosaur(win, timer):
    global ds_x, ds_y, jumpState, jumpValue, dino_show, dino_limit
    if jumpState:
        if ds_y >= dino_limit:
            jumpValue = -10
        if ds_y <= 0:
            jumpValue = 10
        ds_y += jumpValue
        if ds_y >= dino_limit:
            jumpState = False
    win.blit(dino_show[timer % 10 // 5], [ds_x, ds_y])


#***恐龍設定結束***

#===仙人掌設定開始===
cacti_w = img_cacti.get_width()
cacti_h = img_cacti.get_height()
cacti_x = bg_x - 100
cacti_y = LIMIT_LOW
cacti_shift = 10
cacti_dist = int((cacti_w + cacti_h) / 2)


def move_cacti(win):
    global cacti_x, cacti_y, cacti_shift, score, xxx
    cacti_x -= cacti_shift
    win.blit(img_cacti, [cacti_x, cacti_y])
    if cacti_x < 0:
        xxx = random.randint(0, 2)
        score += 1
        cacti_x = bg_x - 100
        cacti_y = LIMIT_LOW


#***仙人掌設定結束***

#===怪物設定開始===
mon_w = img_monster.get_width()
mon_h = img_monster.get_height()
mon_x = bg_x - 100
mon_y = LIMIT_LOW
mon_shift = 10
mon_dist = int((mon_w + mon_h) / 2)


def move_monster(win):
    global mon_x, mon_y, mon_shift, score, xxx
    mon_x -= mon_shift
    win.blit(img_monster, [mon_x, mon_y])
    if mon_x < 0:
        xxx = random.randint(0, 2)
        score += 2
        mon_x = bg_x - 100
        mon_y = LIMIT_LOW


#***怪物設定結束***

#===翼龍設定開始===
ptera_w = img_ptera[0].get_width()
ptera_h = img_ptera[0].get_height()
ptera_x = bg_x - 100
ptera_y = LIMIT_LOW - 30
ptera_shift = 10
ptera_dist = int((ptera_w + ptera_h) / 2)


def move_ptera(win, timer):
    global ptera_x, ptera_y, ptera_shift, score, ds_x, ds_y, xxx
    ptera_x -= ptera_shift
    win.blit(img_ptera[timer % 10 // 5], [ptera_x, ptera_y])
    if ptera_x < 0:
        xxx = random.randint(0, 2)
        score += 1
        ptera_x = bg_x - 100
        ptera_y = LIMIT_LOW - 30


#***翼龍設定結束***


#***碰撞設定開始***
def is_hit(x1, y1, x2, y2, r):
    if ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) < (r * r):
        return True
    else:
        return False


#***碰撞設定結束***

#===GameOver設定開始===
gg = False
gg_img_w = img_gg.get_width()
gg_img_h = img_gg.get_height()


def game_over(win):
    win.blit(img_gg, ((bg_x - gg_img_w) / 2, (bg_y - gg_img_h) / 2))


#***GameOver設定結束***
pygame.mixer.music.load("image/hit.mp3")
#===主程式開始===
while True:
    #===計時與速度===
    clock.tick(20)
    timer += 1
    #===偵測鍵盤事件開始===
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:  #判斷是否按下
            if event.key == K_UP and ds_y >= dino_limit:  #判斷恐龍是否在地上
                jumpState = True  #開啟跳
                pygame.mixer.music.play()
            elif event.key == K_DOWN and jumpState == False:
                dino_show = img_bend_down
                dino_limit = get_dino_limit(dino_show)
                ds_y = dino_limit
            elif event.key == K_RETURN and gg == True:
                gg = False
                cacti_x = bg_x - 100
                ptera_x = bg_x - 100
                mon_x = bg_x - 100
                ds_x = 50
                ds_y = dino_limit
                score = 0
                jumpState = False
        elif event.type == KEYUP:
            if event.key == K_DOWN and jumpState == False:
                dino_show = img_dinosaur
                dino_limit = get_dino_limit(dino_show)
                ds_y = dino_limit
    #===遊戲結束===
    if (gg == True):
        game_over(screen)
    #===遊戲進行===
    else:
        roll_x = (roll_x - 10) % bg_x
        screen.blit(img, [roll_x - bg_x, 0])
        screen.blit(img, [roll_x, 0])
        move_dinosaur(screen, timer)
        get_score(screen)
        if xxx == 0:
            move_cacti(screen)
        if xxx == 1:
            move_monster(screen)
        if xxx == 2:
            move_ptera(screen, timer)
        #===更新角色狀態===
        if (is_hit(ds_x, ds_y, cacti_x, cacti_y, cacti_dist)):
            gg = True
        if (is_hit(ds_x, ds_y, ptera_x, ptera_y, ptera_dist)):
            gg = True
        if (is_hit(ds_x, ds_y, mon_x, mon_y, mon_dist)):
            gg = True
    pygame.display.update()
    #===主程式結束===
