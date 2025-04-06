import pygame
import os

pygame.init()

pygame.mixer.init() #музыка шығару үшін микшер 

screen = pygame.display.set_mode((800, 600))

playlist = [ 
            "1.mp3",
            "2.mp3",
            "3.mp3",
            "4.mp3"
            ]

play_ = 0

pygame.mixer.music.load(playlist[play_])

clock = pygame.transform.scale(pygame.image.load("35019762_8201782.jpg"), (800, 600)) # просто обой

def play_music():
    pygame.mixer.music.play(loops = 0, start = 0.0)
    
def stop_music():
    pygame.mixer.music.stop()
    
def next_music():
    global play_
    play_ = (play_ + 1) % len(playlist) # соңғы трек болса басынан басталуына жауап береді және индекс келесі қосады
    pygame.mixer.music.load(playlist[play_])
    play_music()
    
def prev_music():
    global play_
    play_ = (play_ - 1) % len(playlist) # индекстен бірді азайтады
    pygame.mixer.music.load(playlist[play_]) 
    play_music()
    
    
done = False

while not done:
    for event in pygame.event.get(): # кнопкалар басылғанда орындалатын әрекеттер 
        if event.type == pygame.QUIT:
            done = True
            
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                play_music()
            elif event.key == pygame.K_DOWN:
                stop_music()
            elif event.key == pygame.K_RIGHT:
                next_music()
            elif event.key == pygame.K_LEFT:
                prev_music()
        
    
    screen.blit(clock, (0,0)) # экранға обой шығару
    pygame.display.flip()
    
    