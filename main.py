
import pygame
import sys
import random
from garden import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Noob's farm")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font_pixel = pygame.font.Font("font/Press_Start_2P/PressStart2P-Regular.ttf", 15)


#Button prepare
btn_plant = pygame.Rect(375, 75, 140, 60)
text = font_pixel.render("Plant", True, BLACK)
text_rect = text.get_rect(center=btn_plant.center)

#Text prepare


#Spite Sheet prepare
img_noob_stand = pygame.image.load(f"noob/Stand.png")
lst_img_noob_right = []
for i in range(4):
    img_noob_right = pygame.image.load(f"noob/Right{i+1}.png")
    lst_img_noob_right.append(img_noob_right)
lst_img_noob_left = []
for i in range(4):
    img_noob_left = pygame.image.load(f"noob/Left{i+1}.png")
    lst_img_noob_left.append(img_noob_left)
lst_img_noob_up = []
for i in range(3):
    img_noob_up = pygame.image.load(f"noob/Up{i+1}.png")
    lst_img_noob_up.append(img_noob_up)
lst_img_noob_down = []
for i in range(3):
    img_noob_down = pygame.image.load(f"noob/Down{i+1}.png")
    lst_img_noob_down.append(img_noob_down)
lst_img_corn = []
for i in range(7):
    img_corn = pygame.image.load(f"corn\grow_corn{i+1}.png")
    lst_img_corn.append(img_corn)
img_shop_close = pygame.image.load("shop/seed_shop_close.png")
img_shop_ready = pygame.image.load("shop/seed_shop_ready.png")

#Initial value prepare
running = True
action = 0
timeframe = 0
pos_noob = [200,200]
pos_shop = [350,350]
seed = 3
lst_pos_planted = []
time_start_grow  = 0
while running:
    pygame.time.delay(20)
    screen.fill((0,153,76))

    #Button Zone
    pygame.draw.rect(screen, (200,200,200), btn_plant) #สีปุ่ม
    pygame.draw.rect(screen, BLACK, btn_plant, 2)  # ขอบปุ่ม
    screen.blit(text, text_rect) #ข้อความปุ่ม


    #Event Zone
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:    
            if btn_plant.collidepoint(event.pos):
                lst_pos_planted = planted(seed)
                time_start_grow = timeframe
                seed = 0  
  
    #Keyboard sensing zone
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        action = 1  
        pos_noob[0] -= 5
    if keys[pygame.K_RIGHT]:
        action = 2
        pos_noob[0] += 5
    if keys[pygame.K_UP]:
        action = 3
        pos_noob[1] -= 5
    if keys[pygame.K_DOWN]:
        action = 4
        pos_noob[1] += 5

    #Text Zone
    txt_plant = font_pixel.render(f"Seed: {seed}", True, BLACK)
    txt_rect = txt_plant.get_rect(center=(450, 50))
    screen.blit(txt_plant, txt_rect)

    #Show spite zone
    garden(screen, lst_pos_planted, timeframe, time_start_grow, lst_img_corn)
    #########seed shop###########
    if  ((pos_shop[0]-60 <=pos_noob[0] <= pos_shop[1]+140) and
    (pos_shop[1]-60 <= pos_noob[1] <= pos_shop[1]+80)):

        screen.blit(img_shop_ready, (pos_shop[0],pos_shop[1]))
    else:
        screen.blit(img_shop_close, (pos_shop[0],pos_shop[1]))

    ######### Noob ###########
    if action == 0:
        screen.blit(img_noob_stand, (pos_noob[0],pos_noob[1]))
    if action == 1:
        screen.blit(lst_img_noob_left[timeframe%4], (pos_noob[0],pos_noob[1]))
    if action == 2:
        screen.blit(lst_img_noob_right[timeframe%4], (pos_noob[0],pos_noob[1]))
    if action == 3:
        screen.blit(lst_img_noob_up[timeframe%3], (pos_noob[0],pos_noob[1]))
    if action == 4:
        screen.blit(lst_img_noob_down[timeframe%3], (pos_noob[0],pos_noob[1]))


    #Final value zone
    action = 0
    timeframe += 1
    #close window
    pygame.display.flip()

pygame.quit()
sys.exit()

