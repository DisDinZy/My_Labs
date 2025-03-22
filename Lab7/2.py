import pygame
import os

pygame.init()

# Загрузка плейлиста
playlist = []
music_folder = "C:\\pp22\\pp2\\lab7\\musics"
allmusic = os.listdir(music_folder)

for song in allmusic:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, song))

# Настройки экрана
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Straykids")
clock = pygame.time.Clock()

# Загрузка изображений
background = pygame.image.load("C:\\pp22\\pp2\\lab7\\music-elements\\background1.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Масштабируем, если нужно

# Панель управления
panel_width, panel_height = 500, 100
bg = pygame.Surface((panel_width, panel_height))
bg.fill((255, 255, 255))

font = pygame.font.SysFont(None, 30)

# Загрузка иконок кнопок
btn_size = (60, 60)
playb = pygame.transform.scale(pygame.image.load("C:\\pp22\\pp2\\lab7\\music-elements\\play.png"), btn_size)
pausb = pygame.transform.scale(pygame.image.load("C:\\pp22\\pp2\\lab7\\music-elements\\pause.png"), btn_size)
nextb = pygame.transform.scale(pygame.image.load("C:\\pp22\\pp2\\lab7\\music-elements\\next.png"), btn_size)
prevb = pygame.transform.scale(pygame.image.load("C:\\pp22\\pp2\\lab7\\music-elements\\back.png"), btn_size)

# Индекс текущей песни и статус воспроизведения
index = 0
aplay = False

pygame.mixer.music.load(playlist[index]) 
pygame.mixer.music.play(1)
aplay = True 

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if aplay:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                aplay = not aplay
            if event.key == pygame.K_RIGHT:
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
            if event.key == pygame.K_LEFT:
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

    # Ограничение длины названия трека
    max_length = 30
    song_name = os.path.basename(playlist[index])
    if len(song_name) > max_length:
        song_name = song_name[:max_length] + "..."
    text = font.render(song_name, True, (20, 20, 50))

    # Отрисовка фона по центру экрана
    screen.blit(background, (0, 0))

    # Центрирование панели управления
    panel_x = (WIDTH - panel_width) // 2
    panel_y = HEIGHT - panel_height - 50
    screen.blit(bg, (panel_x, panel_y))

    # Размещение текста по центру панели
    text_x = panel_x + (panel_width - text.get_width()) // 2
    text_y = panel_y + 15
    screen.blit(text, (text_x, text_y))

    # Размещение кнопок
    btn_y = panel_y + 40  # Отступ от верхней границы панели
    screen.blit(prevb, (panel_x + 50, btn_y))
    screen.blit(pausb if aplay else playb, (panel_x + (panel_width - btn_size[0]) // 2, btn_y))
    screen.blit(nextb, (panel_x + panel_width - 110, btn_y))

    clock.tick(24)
    pygame.display.update()