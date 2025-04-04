import pygame, sys
from pygame.locals import *
import time, random

# Инициализация библиотеки pygame
pygame.init()

# Создаем объект для управления FPS
FPS = pygame.time.Clock()

# Цвета, которые будут использоваться в игре
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Переменные для скорости, счета и монет
SPEED = 5
SPEED_COINS = 3
SCORE = 0
COINS = 0

# Шрифты для текста на экране
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

# Создаем надпись "Game Over", которая будет отображаться, если игрок проиграет
game_over = font.render("Game Over", True, BLACK)

# Загружаем фон игры и масштабируем его под нужный размер
background = pygame.transform.scale(pygame.image.load("AnimatedStreet.png"), (400, 600))

# Настроим экран игры
screen = pygame.display.set_mode((400, 600))
screen.fill(WHITE)
pygame.display.set_caption("Racer")

# Определение класса Enemy (враг)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")  # Загружаем изображение врага
        self.rect = self.image.get_rect()  # Получаем прямоугольник для определения границ
        self.rect.center = (random.randint(42, 359), 0)  # Изначальная позиция врага
    
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)  # Враг движется вниз по экрану с заданной скоростью
        if (self.rect.top > 600):  # Если враг выходит за нижнюю границу экрана
            SCORE += 1  # Увеличиваем счет
            self.rect.top = 0  # Возвращаем врага на верхнюю границу экрана
            self.rect.center = (random.randint(42, 359), 0)  # Рандомная позиция по X

# Определение класса Coins (монета)
class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Coin.png"), (40, 40))  # Изображение монеты
        self.rect = self.image.get_rect()  # Прямоугольник для коллизий
        self.rect.center = (random.randint(42, 359), 0)  # Начальная позиция монеты на экране
        
    def move(self):
        global COINS
        self.rect.move_ip(0, SPEED_COINS)  # Двигаем монету вниз по экрану
        if (self.rect.top > 600):  # Если монета выходит за пределы экрана
            self.rect.top = 0  # Ставим её обратно на верх экрана
            self.rect.center = (random.randint(42, 359), 0)  # Рандомное положение монеты

# Определение класса Player (игрок)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")  # Изображение игрока
        self.rect = self.image.get_rect()  # Прямоугольник для коллизий
        self.rect.center = (160, 520)  # Начальная позиция игрока
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()  # Проверяем, какие клавиши нажаты
        if self.rect.left > 40:  # Проверка, чтобы игрок не выходил за левую границу экрана
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)  # Двигаем игрока влево
        if self.rect.right < 359:  # Проверка, чтобы игрок не выходил за правую границу экрана
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)  # Двигаем игрока вправо

# Создаем объекты игрока, врага и монеты
P1 = Player()
E1 = Enemy()
C1 = Coins()

# Группы для врагов, монет и всех спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Устанавливаем таймер для увеличения скорости
INC_Speed = pygame.USEREVENT + 1
pygame.time.set_timer(INC_Speed, 1000)

# Главный игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == INC_Speed:  # Если время вышло, увеличиваем скорость
            if SPEED != 10:
                SPEED += 0.5
        if event.type == QUIT:  # Если игрок закрыл окно игры
            pygame.quit()
            sys.exit()
    
    ps = pygame.key.get_pressed()  # Проверка нажатых клавиш
    if ps[K_TAB]:  # Если нажата клавиша TAB, завершаем игру
        pygame.quit()
        sys.exit()
    
    if ps[K_k]:  # Если нажата клавиша K, проигрываем звук
        pygame.mixer.Sound("1.mp3").play()

    # Отображаем фон и текст
    screen.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)  # Отображаем счет
    screen.blit(scores, (10, 10))
    coinss = font_small.render(str(COINS), True, YELLOW)  # Отображаем количество монет
    screen.blit(coinss, (365, 10))
    
    # Обновляем все спрайты
    for ent in all_sprites:
        screen.blit(ent.image, ent.rect)
        ent.move()  # Двигаем спрайты

    # Проверяем столкновение игрока с монетами
    collected = pygame.sprite.spritecollideany(P1, coins)
    if collected:
        pygame.mixer.Sound("coin-recieved-230517.mp3").play()  # Звук при сборе монеты
        COINS += 1  # Увеличиваем счет монет
        collected.rect.top = 0  # Перемещаем монету обратно в верхнюю часть экрана
        collected.rect.center = (random.randint(42, 359), 0)  # Рандомное положение монеты

    # Проверяем столкновение игрока с врагами
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()  # Звук при столкновении с врагом
        time.sleep(0.5)  # Пауза после столкновения
        
        screen.fill(RED)  # Заливаем экран красным
        screen.blit(game_over, (30, 250))  # Отображаем надпись "Game Over"
        
        pygame.display.update()
        for ent in all_sprites:  # Удаляем все спрайты
            ent.kill()
        time.sleep(2)  # Пауза перед выходом из игры
        pygame.quit()
        sys.exit()

    pygame.display.update()  # Обновляем экран
    FPS.tick(60)  # Устанавливаем количество кадров в секунду
