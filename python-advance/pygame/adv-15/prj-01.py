#===載入套件開始===
import pygame
import sys
import os

os.chdir(sys.path[0])
from pygame.locals import *
import random
#***載入套件結束***
image_gg = pygame.image.load("image/gameover.png")
#===初始化設定開始===
BLOCK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()
clock = pygame.time.Clock()

act = False
#***初始化設定結束***

#===遊戲視窗設定開始===
bg_x = 800
bg_y = 600
bg_size = (bg_x, bg_y)

pygame.display.set_caption(u"打磚塊遊戲")
screen = pygame.display.set_mode(bg_size)

#***遊戲視窗設定結束***

#===磚塊設定開始===
TOTAL_BLOCK = 99
bricks_list = []
brick_num = 0
brick_x = 70
brick_y = 60
brick_w = 0
brick_h = 0
brick_v = True
for i in range(0, TOTAL_BLOCK):
    if i % 11 == 0:
        brick_w = 0
        brick_h += 18
    bricks_list.append(
        [brick_w + brick_x, brick_h + brick_y, 58, 16, brick_v, RED])
    brick_w += +60


def bricks_update(win):
    global brick_num, dy
    for bricks in bricks_list:
        if bricks[4] == True:
            if is_hit(ball_x, ball_y, bricks):
                dy = -dy
                bricks[4] = False
                brick_num -= 1
            block_rect = [bricks[0], bricks[1], bricks[2], bricks[3]]
            pygame.draw.rect(win, bricks[5], block_rect)


#===磚塊設定結束===

#===顯示磚塊數量設定開始===
typeface = pygame.font.get_default_font()
number_font = pygame.font.Font(typeface, 36)
number_font1 = pygame.font.Font(typeface, 36)
lif = 3
a = 0


def get_block_num(win):
    global brick_num
    sur = number_font.render(str(brick_num), True, RED)
    win.blit(sur, [10, 10])


def life(win):
    global lif, a, b
    sur = number_font1.render(str(lif - a), True, (0, 0, 255))
    win.blit(sur, [bg_x - 30, 10])
    if lif - a < 1:
        b = False


#===顯示磚塊數量設定結束===


#===碰撞設定開始===
def is_hit(x, y, boxRect):
    xmatch = x >= boxRect[0] and x <= boxRect[0] + boxRect[2]
    ymatch = y >= boxRect[1] and y <= boxRect[1] + boxRect[3]
    if xmatch and ymatch:
        return True
    return False


#===碰撞設結束===


#===初始遊戲設定開始===
def resetGame():
    global brick_num, bricks_list, dx, dy, act
    for bricks in bricks_list:
        r = random.randint(155, 255)
        g = random.randint(155, 255)
        b = random.randint(155, 255)
        bricks[5] = (r, g, b)
        bricks[4] = True
    act = False
    brick_num = TOTAL_BLOCK
    dx = 8
    dy = -8


#===初始遊戲設定結束===

#===底板設定開始===
paddle_x = 0
paddle_y = (bg_y - 24)


def paddle_update(win):
    global dy
    paddly_rect = [paddle_x, paddle_y, 100, 10]
    pygame.draw.rect(win, RED, paddly_rect)
    if is_hit(ball_x, ball_y, paddly_rect):
        dy = -dy


#===底板設定結束===

#===球設定開始===
ball_x = 100
ball_y = 100
ball_radius = 8
ball_diameter = ball_radius * 2
ball_color = WHITE
dx = 8
dy = -8
b = True


def ball_update(win):
    global ball_x, ball_y
    global dx, dy, act, a
    if act == False:
        ball_x = paddle_x + 50
        ball_y = paddle_y - ball_radius
    else:
        ball_x += dx
        ball_y += dy
        if ball_y > bg_y:
            act = False
            a += 1
        if (ball_x > bg_x - ball_diameter or ball_x < ball_diameter):
            dx = -dx
        if (ball_y < ball_diameter):
            dy = -dy

    pygame.draw.circle(win, ball_color, [ball_x, ball_y], ball_radius)


#===球設定結束===

#===初始遊戲設定開始===
gg_img_w = image_gg.get_width()
gg_img_h = image_gg.get_height()


def gg(win):
    global lif
    win.blit(image_gg, (int(bg_x - gg_img_w) / 2, int(bg_y - gg_img_h) / 2))


#===初始遊戲設定結束===

#-------------------------------------------------------------------------
resetGame()
# 主迴圈.
while True:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            paddle_x = pygame.mouse.get_pos()[0] - 50
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (act == False):
                act = True
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                b = True
                resetGame()
                lif = 3
                a = 0

    screen.fill(BLOCK)
    if b == True:
        paddle_update(screen)
        get_block_num(screen)
        life(screen)
        ball_update(screen)
        if brick_num == 0:
            resetGame()
        else:
            bricks_update(screen)
    else:
        gg(screen)

    pygame.display.update()
    clock.tick(60)
#-------------------------------------------------------------------------