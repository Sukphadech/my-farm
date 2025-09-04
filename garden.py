import pygame
import random

def planted(num_seed):
    lst_pos_seed = []
    x_fruit = random.randint(0,2)
    y_fruit = random.randint(0,2)
    fruit = [x_fruit, y_fruit]
    for i in range(num_seed):
        while fruit in lst_pos_seed:
            x_fruit = random.randint(0,2)
            y_fruit = random.randint(0,2)
            fruit = [x_fruit, y_fruit]
        lst_pos_seed.append(fruit)
    return lst_pos_seed


def garden(screen, lst_pos_planted, timeframe, time_start_grow, lst_img_corn):
    garden_size = [3,3]
    for i in range(garden_size[0]):
        for j in range(garden_size[1]):
            if [i,j] in lst_pos_planted:
                pygame.draw.rect(screen, (255,153,153), (20+(60*i),20+(60*j), 60, 60))
                pygame.draw.rect(screen, (0,0,0), (20+(60*i),20+(60*j), 60, 60), width=1)
                if timeframe-time_start_grow < 100:
                    screen.blit(lst_img_corn[0], (20+(60*i),20+(60*j)))
                elif 100 <=timeframe-time_start_grow< 200:
                    screen.blit(lst_img_corn[1], (20+(60*i),20+(60*j)))
                elif 200 <=timeframe-time_start_grow< 300:
                    screen.blit(lst_img_corn[2], (20+(60*i),20+(60*j)))
                elif 300 <=timeframe-time_start_grow< 400:
                    screen.blit(lst_img_corn[3], (20+(60*i),20+(60*j)))
                elif 400 <=timeframe-time_start_grow< 500:
                    screen.blit(lst_img_corn[4], (20+(60*i),20+(60*j)))
                elif 500 <=timeframe-time_start_grow:
                    screen.blit(lst_img_corn[5], (20+(60*i),20+(60*j)))
            else:
                pygame.draw.rect(screen, (255,209,204), (20+(60*i),20+(60*j), 60, 60))
                pygame.draw.rect(screen, (0,0,0), (20+(60*i),20+(60*j), 60, 60), width=1)



