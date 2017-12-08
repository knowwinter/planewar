# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import time

def main():
    screen = pygame.display.set_mode((480,600),0,32)
    background = pygame.image.load('./feiji/background.png')
    hero = pygame.image.load('./feiji/hero1.png')
    bullet = pygame.image.load('./feiji/bullet.png')
    pygame.key.set_repeat(10)
    x = 190
    y = 476
    bullet_x = x + 50 - 11
    bullet_y = y - 22
    while True:
        screen.blit(background, (0, 0))
        screen.blit(hero, (x, y))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    x -= 10
                    if x < 0:
                        x = 0
                elif event.key == K_d or event.key == K_RIGHT:
                    x += 10
                    if x > 380:
                        x = 380
                elif event.key == K_SPACE:
                    screen.blit(bullet, (bullet_x, bullet_y))
                    pygame.display.update()


        time.sleep(0.01)
if __name__ == "__main__":
    main()