# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import time
import random
from PIL import Image

class Plane(object):
    def __init__(self, screen, x, y, image_path, down_imgs):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.blowups = []
        for down_img in down_imgs:
            self.blowups.append(pygame.image.load(down_img))

        fp = open(image_path, 'r')
        img = Image.open(fp)
        fp.close()
        self.size = (img.size[0], img.size[1])
        self.screen = screen
        self.bullet_list = []

    def display(self, plane):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self. bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)
            if type(plane) != list:
                if self.hit(plane, bullet):
                    plane.crash()
                    if self.bullet_list:
                        self.bullet_list.remove(bullet)
            else:
                for p in plane:
                    if self.hit(p, bullet):
                        if self.bullet_list:
                            self.bullet_list.remove(bullet)
                        p.crash()

                        plane.remove(p)

        if type(plane) != list:
            if self.pang(plane):
                plane.crash()
        else:
            for p in plane:
                if self.pang(p):
                    p.crash()
                    plane.remove(p)
                    self.crash()



    def pang(self, plane):
        if (plane.y + plane.size[1] > self.y and plane.y < self.y + self.size[1] and plane.x + plane.size[0] > self.x and plane.x < self.x + self.size[0]):
            return True
        else:
            return False

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
        self.bullet_list.append(Bullet(self, './feiji/bullet.png'))

    def judge(self):
        if self.y > 600:
            return True
        else:
            return False

    def hit(self, plane, bullet):

        if plane.y + plane.size[1] > 0 and (bullet.y < plane.y + plane.size[1] and bullet.y + bullet.size[1] > plane.y) and (bullet.x + bullet.size[0] > plane.x and bullet.x < plane.x + plane.size[0]):
            return True
        else:
            return False


    def crash(self):
        for blowup in self.blowups:
            self.screen.blit(blowup, (self.x, self.y))


class PlaneHero(Plane):
    pass

class Enemy(Plane):
    def fire(self):
        random_num = random.randint(1, 100)
        if random_num == 8 or random_num == 78:
            self.bullet_list.append(EnemyBullet(self, './feiji/bullet1.png'))

    def hit(self, plane, bullet):

        if (bullet.y + bullet.size[1] > plane.y and bullet.y < plane.y + plane.size[1]) and (bullet.x + bullet.size[0] > plane.x and bullet.x < plane.x + plane.size[0]):
            return True
        else:
            return False





class Bullet(object):
    def __init__(self, plane, image_path):
        fp = open(image_path, 'r')
        img = Image.open(fp)
        fp.close()
        self.size = img.size
        self.x = plane.x + plane.size[0] / 2 - self.size[0] /2
        self.y = plane.y - img.size[1]
        self.image = pygame.image.load(image_path)
        self.screen = plane.screen

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 5

    def judge(self):
        if self.y < 0 - self.size[1]:
            return True
        else:
            return False

class EnemyBullet(Bullet):
    def __init__(self, plane, image_path):
        fp = open(image_path, 'r')
        img = Image.open(fp)
        fp.close()
        self.size = img.size
        self.x = plane.x + plane.size[0] / 2 - self.size[0] /2
        self.y = plane.y + plane.size[1]
        self.image = pygame.image.load(image_path)
        self.screen = plane.screen

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 10

    def judge(self):
        if self.y > 600:
            return True
        else:
            return False

class Screen(object):
    def __init__(self, image_path):
        self.enemy_list = []
        self.background = pygame.image.load(image_path)
        self.screen = pygame.display.set_mode((480, 600), 0, 32)



    def add_enemy(self):
        random_num = random.randint(1, 100)
        if random_num == 8 or random_num == 78:
            self.enemy_list.append(Enemy(self.screen, random.randint(0, 400), -100, './feiji/enemy1.png', ('./feiji/enemy1_down1.png', './feiji/enemy1_down2.png', './feiji/enemy1_down3.png', './feiji/enemy1_down4.png')))

    def display(self):
        hero = PlaneHero(self.screen, 190, 472, './feiji/hero1.png', ('./feiji/hero_blowup_n1.png', './feiji/hero_blowup_n2.png', './feiji/hero_blowup_n3.png', './feiji/hero_blowup_n4.png'))
        pygame.key.set_repeat(10)
        while True:
            self.screen.blit(self.background, (0, 0))
            hero.display(self.enemy_list)
            for enemy in self.enemy_list:
                enemy.display(hero)
                enemy.auto_move()
                enemy.fire()
                if enemy.judge():
                    self.enemy_list.remove(enemy)
            self.add_enemy()
            pygame.display.update()
            key_control(hero)
            key_space(hero)
            time.sleep(0.01)








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
    screen = Screen('./feiji/background.png')


    screen.display()





if __name__ == "__main__":
    main()