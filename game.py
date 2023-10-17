import pygame
import random
import time
from pygame.locals import *


class Person: #описание класса игрового объекта
    def __init__(self, x, y, speed, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(image)

    def move(self): #метод преследования игрока
        if self.x < player.x:
            self.x += self.speed
        elif self.x > player.x:
            self.x -= self.speed
        if self.y < player.y:
            self.y += self.speed
        elif self.y > player.y:
            self.y -= self.speed

        #проверка окончания игры
        global gameovercheck
        #проверка столкновения
        if self.x <= player.x + 64 and self.x >= player.x and self.y >= player.y and self.y <= player.y + 64:
            gameovercheck = True
            screen.blit(gameover, (0, 0))
        if self.x+64 <= player.x + 64 and self.x+64 >= player.x and self.y+64 >= player.y and self.y+64 <= player.y + 64:
            gameovercheck = True
            screen.blit(gameover, (0, 0))


pygame.init()   #инициализация игры, отрисовка окна
screen = pygame.display.set_mode((1280, 720), 0, 32)
pygame.display.set_caption("First Python Game!")
back = pygame.image.load('back.png')
gameover = pygame.image.load('gameover.png')

font = pygame.font.Font(None, 25)
scorefont = pygame.font.Font(None, 60)
score = 0   #количество очков
gameovercheck = False #окончание игры
time0 = time.time()

enemynum = 3
lastadd = 0

player = Person(100, 320, 5, 'player.png') #инициализация игрока
allplayers = [player] #список игровых объектов

abouttext = font.render("GitHub: stepigor. Version 1.0.", True, (255, 255, 255))

mainLoop = True
while mainLoop: #игровой цикл

    if gameovercheck == False:
        
        if score == 3:
            try:
                enemy1
                enemy2
            except:
                #создание первых противников
                enemy1 = Person(1000, 250, 1, 'enemy.png')
                enemy2 = Person(1000, 500, 1, 'enemy.png')
                allplayers.append(enemy1)
                allplayers.append(enemy2)

        if score > 14 and score % 15 == 0 and score != lastadd: #добавление противников каждые 30 очков
            try:
                globals()['enemy' + str(enemynum)]
            except KeyError:
                globals()['enemy' + str(enemynum)] = Person(random.randint(0,1200),random.randint(0,650),random.randint(1,2),'enemy.png');
                allplayers.append(globals()['enemy' + str(enemynum)])
                enemynum += 1
                lastadd = score

        #вычисление количества очков
        time1 = time.time()
        score = int(time1 - time0)
        scoretext = scorefont.render(str(score), True, (255, 255, 255))

        screen.blit(back, (0, 0))
        #отрисовка игровых объектов
        for i, item in enumerate(allplayers):
            screen.blit(item.image, (item.x, item.y))
            if i != 0:
                item.move()

        #управление персонажем
        keys_pressed = pygame.key.get_pressed()
        if (keys_pressed[K_UP] or keys_pressed[K_w]) and player.y > 0:
            player.y -= player.speed
        if (keys_pressed[K_DOWN] or keys_pressed[K_s]) and player.y < 656:
            player.y += player.speed
        if (keys_pressed[K_RIGHT] or keys_pressed[K_d]) and player.x < 1216:
            player.x += player.speed
        if (keys_pressed[K_LEFT] or keys_pressed[K_a]) and player.x > 0:
            player.x -= player.speed

        screen.blit(abouttext, (3, 695))
        screen.blit(scoretext, (1200, 15))

    else:
        #отрисовка проигрыша
        screen.blit(gameover, (0, 0))
        screen.blit(scoretext, (122, 400))
        
        key_press = pygame.key.get_pressed()
        #новая игра
        if key_press[K_RETURN]:
            time0 = time.time()
            time1 = time.time()
            score = 0
            for i in range(1,enemynum):
                del globals()['enemy'+str(i)]
            lastadd = 0
            enemynum = 3
            allplayers = [player]
            gameovercheck = False

    for event in pygame.event.get():
        if event.type == QUIT:
            mainLoop = False

    pygame.display.update()

pygame.quit()