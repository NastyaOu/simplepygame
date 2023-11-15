import pygame
import random
import time
from pygame.locals import *


# описание класса игрового объекта
class Character:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed


class Enemy(Character):
    def __init__(self, x, y, speed):
        super().__init__(x, y, speed)
        self.image = pygame.image.load('enemy.png')

    # метод преследования игрока
    def move(self):
        if self.x < player.x:
            self.x += self.speed
        elif self.x > player.x:
            self.x -= self.speed
        if self.y < player.y:
            self.y += self.speed
        elif self.y > player.y:
            self.y -= self.speed

        # проверка окончания игры
        global game_over_flag
        # проверка столкновения
        if player.x + 64 >= self.x >= player.x and player.y <= self.y <= player.y + 64:
            game_over_flag = True
            screen.blit(game_over, (0, 0))
        if player.x + 64 >= self.x + 64 >= player.x and player.y <= self.y + 64 <= player.y + 64:
            game_over_flag = True
            screen.blit(game_over, (0, 0))


class Player(Character):
    def __init__(self, x, y, speed):
        super().__init__(x, y, speed)
        self.image = pygame.image.load('player.png')

    # управление персонажем
    def move(self):
        keys_pressed = pygame.key.get_pressed()
        if (keys_pressed[K_UP] or keys_pressed[K_w]) and self.y > 0:
            self.y -= self.speed
        if (keys_pressed[K_DOWN] or keys_pressed[K_s]) and self.y < 656:
            self.y += self.speed
        if (keys_pressed[K_RIGHT] or keys_pressed[K_d]) and self.x < 1216:
            self.x += self.speed
        if (keys_pressed[K_LEFT] or keys_pressed[K_a]) and self.x > 0:
            self.x -= self.speed


# инициализация игры, отрисовка окна
pygame.init()
screen = pygame.display.set_mode((1280, 720), 0, 32)
pygame.display.set_caption("First Python Game!")
back = pygame.image.load('back.png')
game_over = pygame.image.load('gameover.png')

font = pygame.font.Font(None, 25)
score_font = pygame.font.Font(None, 60)

# количество очков
score = 0
score_text = score_font.render(str(score), True, (255, 255, 255))

# окончание игры
game_over_flag = False
time_start = time.time()
last_add = 0

# инициализация игрока
player = Player(100, 320, 5)

# список игровых объектов
characters = [player]

about_text = font.render("GitHub: stepigor. Version 1.0.", True, (255, 255, 255))

mainLoop = True
# игровой цикл
while mainLoop:
    if not game_over_flag:

        if score == 3 and score != last_add:
            characters.append(Enemy(1000, 250, 1))
            characters.append(Enemy(1000, 750, 1))
            last_add = score

        # добавление противников каждые 15 очков
        if score > 14 and score % 15 == 0 and score != last_add:
            characters.append(Enemy(random.randint(0, 1200), random.randint(0, 650),
                                    random.randint(1, 2)))
            last_add = score

        # вычисление количества очков
        time_now = time.time()
        score = int(time_now - time_start)
        score_text = score_font.render(str(score), True, (255, 255, 255))

        screen.blit(back, (0, 0))
        # отрисовка игровых объектов
        for item in characters:
            screen.blit(item.image, (item.x, item.y))
            item.move()

        screen.blit(about_text, (3, 695))
        screen.blit(score_text, (1200, 15))

    else:
        # отрисовка проигрыша
        screen.blit(game_over, (0, 0))
        screen.blit(score_text, (122, 400))

        key_press = pygame.key.get_pressed()
        # новая игра
        if key_press[K_RETURN]:
            time_start = time.time()
            time_now = time.time()
            score = 0
            last_add = 0
            characters = [player]
            game_over_flag = False

    for event in pygame.event.get():
        if event.type == QUIT:
            mainLoop = False

    pygame.display.update()

pygame.quit()
