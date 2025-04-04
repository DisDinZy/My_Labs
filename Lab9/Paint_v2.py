import pygame  # Импортируем библиотеку Pygame, которая предоставляет функциональность для создания игр и графики.
import sys  # Импортируем модуль sys для работы с системой (например, для завершения программы).

# инициализация pygame
pygame.init()  # Инициализируем все модули Pygame, чтобы начать работу с ними.

# устанавливаем шрифт
font = pygame.font.SysFont("Arial", 15)  # Создаем шрифт "Arial" размером 15 для отображения текста.

# размеры окна
width = 800  # Устанавливаем ширину окна.
height = 600  # Устанавливаем высоту окна.
screen = pygame.display.set_mode((width, height))  # Создаем окно с заданными размерами.
pygame.display.set_caption("PAINT")  # Устанавливаем заголовок окна.

# определяем цвета
black = (0, 0, 0)  # Определяем цвет черный (RGB).
green = (0, 255, 0)  # Определяем цвет зеленый (RGB).
red = (255, 0, 0)  # Определяем цвет красный (RGB).
blue = (0, 0, 255)  # Определяем цвет синий (RGB).
white = (255, 255, 255)  # Определяем цвет белый (RGB).

# начальные параметры рисования
size = 5  # Устанавливаем начальный размер кисти (толщина линии).
color = black  # Устанавливаем начальный цвет рисования (черный).
drawing = False  # Флаг, указывающий на то, рисуется ли что-то в данный момент.
shape = "line"  # Устанавливаем форму рисования по умолчанию (линия).

# часы для регулирования частоты кадров
clock = pygame.time.Clock()  # Создаем объект для управления частотой кадров.

# функции рисования
def draw_line(start, end, color, size):  # Функция для рисования линии.
    pygame.draw.line(screen, color, start, end, size)  # Рисуем линию между двумя точками с заданным цветом и толщиной.

def draw_rect(start, end, color, size):  # Функция для рисования прямоугольника.
    width = abs(start[0] - end[0])  # Вычисляем ширину прямоугольника.
    height = abs(start[1] - end[1])  # Вычисляем высоту прямоугольника.
    pygame.draw.rect(screen, color, (min(start[0], end[0]), min(start[1], end[1]), width, height), size)  # Рисуем прямоугольник.

def draw_circle(start, end, color, size):  # Функция для рисования круга.
    radius = int(((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5)  # Вычисляем радиус круга.
    pygame.draw.circle(screen, color, start, radius, size)  # Рисуем круг.

def erase(start, end, size):  # Функция для стирания (используется белый цвет).
    pygame.draw.circle(screen, white, start, size)  # Рисуем круг белого цвета, чтобы "стереть" часть изображения.

# добавленные фигуры
def draw_square(start, end, color, size):  # Функция для рисования квадрата.
    side = min(abs(start[0] - end[0]), abs(start[1] - end[1]))  # Вычисляем сторону квадрата.
    pygame.draw.rect(screen, color, (min(start[0], end[0]), min(start[1], end[1]), side, side), size)  # Рисуем квадрат.

def draw_right_triangle(start, end, color, size):  # Функция для рисования прямоугольного треугольника.
    base = abs(start[0] - end[0])  # Вычисляем основание треугольника.
    height = abs(start[1] - end[1])  # Вычисляем высоту треугольника.
    points = [(start[0], start[1]), (start[0] + base, start[1]), (start[0], start[1] + height)]  # Определяем вершины треугольника.
    pygame.draw.polygon(screen, color, points, size)  # Рисуем треугольник.

def draw_equilateral_triangle(start, end, color, size):  # Функция для рисования равностороннего треугольника.
    side = int(((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5)  # Вычисляем длину стороны треугольника.
    height = int((3 ** 0.5 / 2) * side)  # Вычисляем высоту равностороннего треугольника.
    points = [(start[0], start[1]), (start[0] + side, start[1]), (start[0] + side / 2, start[1] - height)]  # Определяем вершины треугольника.
    pygame.draw.polygon(screen, color, points, size)  # Рисуем треугольник.

def draw_rhombus(start, end, color, size):  # Функция для рисования ромба.
    width = abs(start[0] - end[0])  # Вычисляем ширину ромба.
    height = abs(start[1] - end[1])  # Вычисляем высоту ромба.
    points = [(start[0], start[1] - height),  # Определяем вершины ромба.
              (start[0] + width, start[1]), 
              (start[0], start[1] + height), 
              (start[0] - width, start[1])]
    pygame.draw.polygon(screen, color, points, size)  # Рисуем ромб.

# заполнение экрана белым
screen.fill(white)  # Заполняем экран белым цветом.

# основной цикл программы
running = True  # Флаг для основного цикла программы.
while running:  # Основной цикл программы.
    for event in pygame.event.get():  # Проверяем все события.
        if event.type == pygame.QUIT:  # Если окно закрывается.
            running = False  # Выходим из цикла.
        if event.type == pygame.MOUSEBUTTONDOWN:  # Если нажата кнопка мыши.
            drawing = True  # Устанавливаем флаг рисования в True.
            last_pos = event.pos  # Сохраняем текущую позицию мыши.
            draw_start_pos = event.pos  # Сохраняем начальную позицию для рисования.
        if event.type == pygame.MOUSEBUTTONUP:  # Если кнопка мыши отпущена.
            drawing = False  # Устанавливаем флаг рисования в False.
        if event.type == pygame.MOUSEMOTION:  # Если мышь двигается.
            if drawing:  # Если рисуем.
                # рисуем в зависимости от выбранной формы
                if shape == "line":
                    draw_line(last_pos, event.pos, color, size)  # Рисуем линию.
                elif shape == "rect":
                    draw_rect(draw_start_pos, event.pos, color, size)  # Рисуем прямоугольник.
                elif shape == "circle":
                    draw_circle(draw_start_pos, event.pos, color, size)  # Рисуем круг.
                elif shape == "eraser":
                    erase(last_pos, event.pos, size)  # Используем ластик.
                elif shape == "square":
                    draw_square(draw_start_pos, event.pos, color, size)  # Рисуем квадрат.
                elif shape == "right_triangle":
                    draw_right_triangle(draw_start_pos, event.pos, color, size)  # Рисуем прямоугольный треугольник.
                elif shape == "equilateral_triangle":
                    draw_equilateral_triangle(draw_start_pos, event.pos, color, size)  # Рисуем равносторонний треугольник.
                elif shape == "rhombus":
                    draw_rhombus(draw_start_pos, event.pos, color, size)  # Рисуем ромб.
                last_pos = event.pos  # Обновляем последнюю позицию мыши.

        if event.type == pygame.KEYDOWN:  # Если нажата клавиша.
            # управление выбором формы
            if event.key == pygame.K_r:
                shape = "rect"  # Выбираем прямоугольник.
            elif event.key == pygame.K_c:
                shape = "circle"  # Выбираем круг.
            elif event.key == pygame.K_e:
                shape = "eraser"  # Выбираем ластик.
            elif event.key == pygame.K_l:
                shape = "line"  # Выбираем линию.
            elif event.key == pygame.K_s:
                shape = "square"  # Выбираем квадрат.
            elif event.key == pygame.K_t:
                shape = "right_triangle"  # Выбираем прямоугольный треугольник.
            elif event.key == pygame.K_y:
                shape = "equilateral_triangle"  # Выбираем равносторонний треугольник.
            elif event.key == pygame.K_h:
                shape = "rhombus"  # Выбираем ромб.

            # управление выбором цвета
            elif event.key == pygame.K_1:
                color = black  # Выбираем черный цвет.
            elif event.key == pygame.K_2:
                color = red  # Выбираем красный цвет.
            elif event.key == pygame.K_3:
                color = blue  # Выбираем синий цвет.
            elif event.key == pygame.K_4:
                color = green  # Выбираем зеленый цвет.

    # вывод инструкций
    text_rect = font.render("press r to draw rectangle", True, black)  # Текст для инструкции по рисованию прямоугольника.
    text_circle = font.render("press c to draw circle", True, black)  # Текст для инструкции по рисованию круга.
    text_line = font.render("press l to draw line", True, black)  # Текст для инструкции по рисованию линии.
    text_eraser = font.render("press e to draw eraser", True, black)  # Текст для инструкции по использованию ластика.
    
    text_square = font.render("press s to draw square", True, black)  # Текст для инструкции по рисованию квадрата.
    text_right_triangle = font.render("press t to draw right triangle", True, black)  # Текст для инструкции по рисованию прямоугольного треугольника.
    text_equilateral_triangle = font.render("press y to draw equilateral triangle", True, black)  # Текст для инструкции по рисованию равностороннего треугольника.
    text_rhombus = font.render("press h to draw rhombus", True, black)  # Текст для инструкции по рисованию ромба.
    
    # отображение текста на экране
    screen.blit(text_rect, (10, 10))  # Отображаем текст на экране.
    screen.blit(text_circle, (10, 25))
    screen.blit(text_line, (10, 40))
    screen.blit(text_eraser, (10, 55))
    screen.blit(text_square, (10, 70))
    screen.blit(text_right_triangle, (10, 85))
    screen.blit(text_equilateral_triangle, (10, 100))
    screen.blit(text_rhombus, (10, 115))

    # инструкции по выбору цветов
    screen.blit(font.render("press 1 to change color - black", True, black), (625, 10))
    screen.blit(font.render("press 2 to change color - red", True, red), (625, 25))
    screen.blit(font.render("press 3 to change color - blue", True, blue), (625, 40))
    screen.blit(font.render("press 4 to change color - green", True, green), (625, 55))

    pygame.display.update()  # Обновляем экран.
    clock.tick(60)  # Ограничиваем частоту кадров до 60 кадров в секунду.

pygame.quit()  # Закрываем Pygame.
sys.exit()  # Выход из программы.
