import pygame 
import time 
import math 

pygame.init() #Pygame ді инициализировать етеді

screen = pygame.display.set_mode((800, 600))

left = pygame.image.load("sec_hand.png")
right = pygame.image.load("min_hand.png")
background = pygame.transform.scale(pygame.image.load("clock.png"), (800, 600)) #задний фонды подгонять етеміз

clock = pygame.time.Clock()

done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #егер кнопка басылса және ол ЕСК болса программа жабу
            done = True
        
    
    
    time_ = time.localtime()
    minute = time_.tm_min + 10 #уақытты дұрыстау 
    sec = time_.tm_sec - 10 
    
    minute_rt = minute * 6  + (sec / 60) * 6 #минут стрелка уголын анықтау
    sec_rt = sec * 6 #үйткені бір секунд 6 градус
    
    screen.blit(background, (0,0)) # фонды шығару (таңалған бет үстіне сурет салу), бірінші шығатын сурет, екінші шығу координатасы
    
    rotated_r = pygame.transform.rotate(right, -minute_rt)
    righter = rotated_r.get_rect(center = (screen.get_width() // 2, screen.get_height() // 2)) #центрін тауып орналастыру 
    screen.blit(rotated_r, righter)
    
    rotated_l = pygame.transform.rotate(left, -sec_rt)
    lefter = rotated_l.get_rect(center = (screen.get_width() // 2, screen.get_height() // 2)) 
    screen.blit(rotated_l, lefter)
    
    pygame.display.flip() #экранды обновлять етеді
    
    clock.tick(120)
    
    
    
