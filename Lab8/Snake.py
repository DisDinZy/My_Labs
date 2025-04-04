import pygame, random
from pygame.locals import *

# Инициализация pygame
pygame.init()  # Инициализация всех модулей pygame
pygame.display.set_caption("Snake")  # Устанавливаем название окна игры

# Определение цветов
GREEN = (0, 255, 0)  # Зеленый для змейки
RED = (255, 0, 0)  # Красный для еды
WHITE = (255, 255, 255)  # Белый для фона
BLACK = (0, 0, 0)  # Черный для текста (по умолчанию)
BLUE = (0, 0, 255)  # Синий для счета
ORANGE = (255, 84, 0)  # Оранжевый для уровня

# Размеры экрана и блоков
sc_width = 800  # Ширина экрана
sc_height = 600  # Высота экрана

snake_block = 25  # Размер блока змейки
snake_speed = 15  # Начальная скорость змейки

# Установка FPS
FPS = pygame.time.Clock()  # Контролируем скорость игры

# Экран
screen = pygame.display.set_mode((sc_width, sc_height))  # Устанавливаем размер экрана

# Шрифты
font_style = pygame.font.SysFont("Verdana", 30)  # Шрифт для сообщений
font_small = pygame.font.SysFont("bahnschrift", 15)  # Шрифт для мелких сообщений
score_font = pygame.font.SysFont("comicsansms", 25)  # Шрифт для счета
level_font = pygame.font.SysFont("comicsansms", 25)  # Шрифт для уровня

# Функция для отображения счета
def Your_score(score):
    value = score_font.render(" " + str(score), True, BLUE)  # Отображаем текущий счет
    screen.blit(value, [0, 0])  # Размещаем счет в верхнем левом углу экрана

# Функция для отображения уровня
def display_level(level):
    levels = level_font.render(" " + str(level), True, ORANGE)  # Отображаем текущий уровень
    screen.blit(levels, (760, 0))  # Размещаем уровень в верхнем правом углу экрана

# Функция для отрисовки змейки
def our_snake(snake_block, snake_list):
    for x in snake_list:  # Проходим по всем частям змейки
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])  # Рисуем прямоугольник для каждого блока змейки

# Функция для отображения сообщений
def message(msg, color):
    mesg = font_style.render(msg, True, color)  # Создаем текст сообщения
    screen.blit(mesg, [100, sc_height / 3])  # Размещаем сообщение по центру экрана

# Функция для генерации случайной позиции еды
def generate_food():
    return round(random.randrange(0, sc_width - snake_block) / 25.0) * 25.0, round(random.randrange(0, sc_height - snake_block) / 25.0) * 25.0
    # Возвращаем случайную позицию для еды, округленную до ближайшего размера блока змейки

# Функция для проверки, не находится ли еда на змейке
def is_food_on_snake(foodx, foody, snake_List):
    for block in snake_List:  # Проверяем, не находит ли еда на одном из блоков змейки
        if block[0] == foodx and block[1] == foody:
            return True  # Если еда на змейке, возвращаем True
    return False  # Если нет, возвращаем False

# Главная функция игры
def gameLoop():
    level = 1  # Начальный уровень
    snake_speed = 15  # Начальная скорость змейки
    game = True  # Флаг для основного игрового цикла
    game_close = False  # Флаг для завершения игры после поражения

    # Начальные координаты змейки
    x1 = sc_width / 2  # Центр экрана по оси X
    y1 = sc_height / 2  # Центр экрана по оси Y
    x1_change = 0  # Начальное изменение по оси X
    y1_change = 0  # Начальное изменение по оси Y

    # Список для хранения тела змейки
    snake_List = []  # Список с блоками змейки
    Length_of_Snake = 1  # Начальная длина змейки

    # Генерация еды
    foodx, foody = generate_food()  # Генерируем первую еду

    # Основной игровой цикл
    while game:

        # Если игра завершена
        while game_close == True:
            screen.fill(WHITE)  # Очищаем экран
            message("You Lost! Press Q-Quit or C-Play Again", RED)  # Сообщение о проигрыше
            Your_score(Length_of_Snake - 1)  # Показываем счет
            pygame.display.update()

            # Обработка событий после окончания игры
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_q:  # Выход из игры
                        game = False
                        game_close = False
                    if event.key == K_c:  # Перезапуск игры
                        gameLoop()  # Рекурсивный вызов для перезапуска игры

        # Обработка событий во время игры
        for event in pygame.event.get():
            if event.type == QUIT:
                game = False
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        # Проверка на выход за границы экрана
        if x1 >= sc_width or x1 < 0 or y1 >= sc_height or y1 < 0:
            game_close = True  # Если змейка выходит за границу, игра заканчивается

        # Обновляем координаты змейки
        x1 += x1_change
        y1 += y1_change
        screen.fill(WHITE)  # Очищаем экран

        # Рисуем еду
        pygame.draw.rect(screen, RED, [foodx, foody, snake_block, snake_block])

        # Создаем голову змейки
        snake_Head = []  # Создаем новый блок для головы змейки
        snake_Head.append(x1)  # Добавляем координаты головы
        snake_Head.append(y1)  # Добавляем координаты головы
        snake_List.append(snake_Head)  # Добавляем голову в тело змейки
        if len(snake_List) > Length_of_Snake:  # Если длина змейки больше необходимой
            del snake_List[0]  # Убираем последний элемент (старую часть змейки)

        # Проверка на столкновение с телом змейки
        for x in snake_List[:-1]:  # Проходим по всем частям змейки, кроме головы
            if x == snake_Head:  # Если голова сталкивается с телом
                game_close = True  # Заканчиваем игру

        # Отображаем змейку
        our_snake(snake_block, snake_List)
        Your_score(Length_of_Snake - 1)  # Отображаем счет
        display_level(level)  # Отображаем уровень
        
        pygame.display.update()  # Обновляем экран

        # Проверка на столкновение с едой
        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food()  # Генерируем новую еду
            # Генерация новой еды, если она попала на змейку
            while is_food_on_snake(foodx, foody, snake_List):
                foodx, foody = generate_food()

            Length_of_Snake += 1  # Увеличиваем длину змейки

            # Увеличиваем уровень каждые 5 съеденных кусочков пищи
            if Length_of_Snake % 5 == 0:
                level += 1
                snake_speed += 1  # Увеличиваем скорость игры

        # Контролируем скорость игры
        FPS.tick(snake_speed)

    pygame.quit()  # Завершаем работу pygame
    quit()  # Завершаем игру

gameLoop()  # Запуск игры
