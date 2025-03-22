import pygame 
import time
import math
pygame.init()


screen = pygame.display.set_mode((800, 600)) #экран размері пиксельмен 
clock = pygame.time.Clock()


leftarm = pygame.image.load("sec_hand.png")
rightarm = pygame.image.load("min_hand.png")
mainclock = pygame.transform.scale(pygame.image.load("clock.png"), (800, 600)) #суретті размеріне келтіру

done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current_time = time.localtime() #localtime уақыт
    minute = current_time.tm_min
    second = current_time.tm_sec
    
    
    
    minute_angle = minute_angle = minute * 6 + (second / 60) * 6 #қазіргі минут * 360 градус / 60 минут + қазіргі секундты қосамыз 
    second_angle = second * 6  
    
  
    screen.blit(mainclock, (0,0)) #фонды шығару
    
    # Правильный поворот с учетом центра изображения
    rotated_rightarm = pygame.transform.rotate(rightarm, -minute_angle)
    rightarmrect = rotated_rightarm.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))  # Центр экрана
    screen.blit(rotated_rightarm, rightarmrect)

    rotated_leftarm = pygame.transform.rotate(leftarm, -second_angle)
    leftarmrect = rotated_leftarm.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))  # Центр экрана
    screen.blit(rotated_leftarm, leftarmrect)

    
    pygame.display.flip() #экранды жаңарту
    clock.tick(120) #fps
    
pygame.quit()