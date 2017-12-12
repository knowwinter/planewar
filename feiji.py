# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import time
import random

class Plane(object):
    def __init__(self, screen, x, y, image_path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.screen = screen
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self. bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)

    def move_left(self):
        self.x -= 10
        if self.x < 0:
            self.x = 0

    def move_right(self):
        self.x += 10
        if self.x > 380:
            self.x = 380

    def auto_move(self):
        self.y += 3
        # if self.x <= 240:
        #     self.x += random.randint(10, 200)
        # else:
        #     self.x -= random.randint(10, 200)

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

class PlaneHero(Plane):
    pass

class Enemy(Plane):
    def fire(self):
        random_num = random.randint(1, 100)
        if random_num == 8 or random_num == 78:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))




class Bullet(object):
    def __init__(self, screen, plane_x, plane_y):
        self.x = plane_x + 50 - 11
        self.y = plane_y - 22
        self.image = pygame.image.load('./feiji/bullet.png')
        self.screen = screen

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 5

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

class EnemyBullet(object):
    def __init__(self, screen, plane_x, plane_y):
        self.x = plane_x + 34.5 - 4.5
        self.y = plane_y + 89
        self.image = pygame.image.load('./feiji/bullet1.png')
        self.screen = screen

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 10

    def judge(self):
        if self.y > 600:
            return True
        else:
            return False


def key_control(hero):
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        # elif event.type == KEYDOWN:
        #     if event.key == K_a or event.key == K_LEFT:
        #         hero.move_left()
        #     elif event.key == K_d or event.key == K_RIGHT:
        #         hero.move_right()
        #     elif event.key == K_SPACE:
        #         hero.fire()
        elif keys[K_a] or keys[K_LEFT]:
            hero.move_left()
        elif keys[K_d] or keys[K_RIGHT]:
            hero.move_right()


def key_space(hero):
    keys = pygame.key.get_pressed()
    if keys[K_SPACE]:
        hero.fire()

def main():
    screen = pygame.display.set_mode((480,600),0,32)
    background = pygame.image.load('./feiji/background.png')
    hero = PlaneHero(screen, 190, 472, './feiji/hero1.png')
    bullet = Bullet(screen,hero.x, hero.y)
    enemy = Enemy(screen, 0, 0, './feiji/enemy1.png')
    pygame.key.set_repeat(10)
    while True:
        screen.blit(background, (0, 0))
        hero.display()
        enemy.display()
        enemy.auto_move()
        enemy.fire()
        # bullet.display()
        pygame.display.update()
        key_control(hero)
        key_space(hero)

                    # pygame.display.update()


        time.sleep(0.01)
if __name__ == "__main__":
    main()