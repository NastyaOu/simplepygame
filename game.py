import pygame
import random
from pygame.locals import *


class Person:
    def __init__(self, x, y, speed, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(image)

    def move(self):
        if self.x < player.x:
            self.x += self.speed
        elif self.x > player.x:
            self.x -= self.speed
        if self.y < player.y:
            self.y += self.speed
        elif self.y > player.y:
            self.y -= self.speed

        if self.x <= player.x + 64 and self.x >= player.x and self.y >= player.y and self.y <= player.y + 64:
            global gameovercheck
            gameovercheck = True
            screen.blit(gameover, (0, 0))


pygame.init()
screen = pygame.display.set_mode((1280, 720), 0, 32)
pygame.display.set_caption("First Python Game!")
back = pygame.image.load('back.png')
gameover = pygame.image.load('gameover.png')

font = pygame.font.Font(None, 25)
scorefont = pygame.font.Font(None, 60)
score = 0
gameovercheck = False

player = Person(100, 300, 2, 'player.png')
enemy1 = Person(1000, 200, 0.5, 'enemy.png')
enemy2 = Person(1000, 400, 1, 'enemy.png')
allplayers = [player, enemy1, enemy2]

abouttext = font.render("GitHub: stepigor. Version 1.0.", True, (255, 255, 255))

mainLoop = True
while mainLoop:

    if gameovercheck == False:

        if score == 30:
            try:
                enemy3
            except:
                enemy3 = Person(random.randint(0, 1200), random.randint(0, 650), 1, 'enemy.png')
                allplayers.append(enemy3)
        if score == 50:
            try:
                enemy4
            except:
                enemy4 = Person(random.randint(0, 1200), random.randint(0, 650), random.randint(1, 2), 'enemy.png')
                allplayers.append(enemy4)
        if score == 70:
            try:
                enemy5
            except:
                enemy5 = Person(random.randint(0, 1200), random.randint(0, 650), random.randint(1, 3), 'enemy.png')
                allplayers.append(enemy5)
        if score == 100:
            try:
                enemy6
            except:
                enemy6 = Person(random.randint(0, 1200), random.randint(0, 650), random.randint(2, 5), 'enemy.png')
                allplayers.append(enemy6)

        ticks = pygame.time.get_ticks()
        score = int(ticks / 1000 % 60)
        scoretext = scorefont.render(str(score), True, (255, 255, 255))

        screen.blit(back, (0, 0))

        for i, item in enumerate(allplayers):
            screen.blit(item.image, (item.x, item.y))
            if i != 0:
                item.move()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_d] and player.x < 1216:
            player.x += player.speed
        if keys_pressed[K_a] and player.x > 0:
            player.x -= player.speed
        if keys_pressed[K_w] and player.y > 0:
            player.y -= player.speed
        if keys_pressed[K_s] and player.y < 656:
            player.y += player.speed

        screen.blit(abouttext, (3, 695))
        screen.blit(scoretext, (1200, 15))

    else:

        screen.blit(gameover, (0, 0))
        screen.blit(scoretext, (122, 400))

    for event in pygame.event.get():
        if event.type == QUIT:
            mainLoop = False

    pygame.display.update()

pygame.quit()