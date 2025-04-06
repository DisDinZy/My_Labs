import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
Clock = pygame.time.Clock()

Back = (255, 255, 255)
Circle = (255, 0, 0)

ball_rad = 25
ball_x = 400
ball_y = 300
ball_speed = 20


done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    but = pygame.key.get_pressed()    #басылып тұрған клавишаны сақтайды
    if but[pygame.K_UP] and ball_y - ball_rad > 0 : ball_y -= ball_speed# радисуы мен қазіргі координата соотношениясы экранның значениясымен салыстыру
    if but[pygame.K_DOWN]and ball_y + ball_rad < 600: ball_y += ball_speed
    if but[pygame.K_LEFT]and ball_x - ball_rad > 0: ball_x -= ball_speed
    if but[pygame.K_RIGHT]and ball_x + ball_rad < 800: ball_x += ball_speed
    
    screen.fill(Back) # артқы фонды қояды
    
    pygame.draw.circle(screen, Circle,(ball_x, ball_y), ball_rad ) #шеңберді салады
    
    
    pygame.display.flip() # обновление
    Clock.tick(120) #FPS