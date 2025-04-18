import psycopg2  # PostgreSQL-мен байланыс үшін кітапхана
import pygame  # Ойын графикасы үшін кітапхана
import sys      # Жүйелік функциялар үшін
import random   # Кездейсоқ сандар үшін
import time     # Уақыт функциясы үшін

# Базамен байланыс
conn = psycopg2.connect(
    dbname='BAzA',             # Дерекқордың аты
    user='postgres',           # Пайдаланушы аты
    password='12345678',       # Құпия сөз
    host='localhost',          # Хост (жергілікті)
    port='5432'                # PostgreSQL порты
)
cur = conn.cursor()  # SQL сұраныстарын орындау үшін курсор жасау

# Қолданушылар кестесін құру
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,             -- Бірегей ID
        username VARCHAR(50) UNIQUE        -- Қолданушы аты (қайталанбайтын)
    );
""")

# Қолданушы ұпайларының кестесін құру
cur.execute("""
    CREATE TABLE IF NOT EXISTS user_score (
        id SERIAL PRIMARY KEY,                           -- Бірегей ID
        user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,  -- Байланыс users кестесімен
        score INTEGER,                                   -- Ұпай
        level INTEGER,                                   -- Деңгей
        saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP     -- Сақтау уақыты
    );
""")
conn.commit()  # Өзгерістерді сақтау

# Қолданушыдан атын сұрау
username = input("Атыңды енгіз: ").strip()  # Атын енгізу
user_id = None  # Қолданушы ID
score = 0       # Ұпай бастапқы
level = 1       # Деңгей бастапқы

# Қолданушы бар ма, тексеру
cur.execute("SELECT id FROM users WHERE username = %s", (username,))
user = cur.fetchone()

if user:
    user_id = user[0]  # Қолданушы ID алу
    cur.execute("SELECT score, level FROM user_score WHERE user_id = %s ORDER BY saved_at DESC LIMIT 1", (user_id,))
    row = cur.fetchone()
    score = row[0] if row else 0  # Соңғы ұпайды алу
    level = row[1] if row else 1  # Соңғы деңгейді алу
    print(f"{username} табылды. {level}-деңгейден бастаймыз.")
else:
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]  # Жаңа қолданушыны тіркеу
    conn.commit()
    print(f"Жаңа қолданушы {username} тіркелді. Ойын 1-деңгейден басталады.")

print("Ойын 2 секундтан кейін басталады...")
time.sleep(2)  # Кішкене кідіріс

# Pygame параметрлерін орнату
pygame.init()
WIDTH, HEIGHT = 600, 400  # Терезе өлшемі
GRID_SIZE = 20  # Тор өлшемі
WHITE, GREEN, RED, BLACK, YELLOW, GG = (255, 128, 0), (0, 255, 0), (255, 0, 0), (255, 255, 255), (255, 255, 0), (0,0,0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
speed = 10 + level * 2  # Деңгейге байланысты жылдамдық

# Тамақ жасау функциясы
def generate_food(snake):
    while True:
        x = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE
        y = random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
        if (x, y) not in snake:
            return (x, y)

# Негізгі ойын функциясы
def game():
    global score, level, speed
    running = True
    while running:
        # Жылан мен тағамды бастау
        snake = [(100, 100), (80, 100), (60, 100)]
        direction = (GRID_SIZE, 0)
        food = generate_food(snake)
        speed = 10 + level * 2
        game_over = False

        while not game_over:
            screen.fill(BLACK)  # Экранды тазалау

            for event in pygame.event.get():  # Пернелерді оқу
                if event.type == pygame.QUIT:
                    pygame.quit()
                    cur.close()
                    conn.close()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != (0, GRID_SIZE):
                        direction = (0, -GRID_SIZE)
                    elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != (0, -GRID_SIZE):
                        direction = (0, GRID_SIZE)
                    elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != (GRID_SIZE, 0):
                        direction = (-GRID_SIZE, 0)
                    elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != (-GRID_SIZE, 0):
                        direction = (GRID_SIZE, 0)
                    elif event.key == pygame.K_p:
                        paused = True
                        pause_text = font.render(" Пауза - кез келген батырма", True, WHITE)
                        screen.blit(pause_text, (WIDTH // 2 - 180, HEIGHT // 2))
                        pygame.display.flip()
                        
                        # Пауза кезінде ұпайды сақтау
                        cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)",
                                    (user_id, score, level))
                        conn.commit()
                        print("⏸ Пауза кезінде нәтиже сақталды.")
                        while paused:
                            for pause_event in pygame.event.get():
                                if pause_event.type == pygame.KEYDOWN:
                                    paused = False

            # Жаңа басты координатаны есептеу
            new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
            if (new_head[0] < 0 or new_head[0] >= WIDTH or
                new_head[1] < 0 or new_head[1] >= HEIGHT or
                new_head in snake):
                game_over = True
                break

            snake.insert(0, new_head)  # Жылан алға жылжиды

            if new_head == food:  # Егер тағам жеген болса
                score += 1
                if score % 3 == 0:  # Әр 3 ұпай сайын деңгей өседі
                    level += 1
                    speed += 2
                food = generate_food(snake)  # Жаңа тағам
            else:
                snake.pop()  # Соңғысын алып тастау

            # Тағам мен жыланды салу
            pygame.draw.rect(screen, RED, (*food, GRID_SIZE, GRID_SIZE))
            for segment in snake:
                pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))

            # Ұпай мен деңгейді экранда көрсету
            score_text = font.render(f"{username}: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))
            score_text = font.render(f"Level: {level}", True, GG)
            screen.blit(score_text, (500, 10))

            pygame.display.flip()
            clock.tick(speed)  # Жаңарту жылдамдығы

        # Ойын аяқталғанда базаға сақтау
        cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)",
                    (user_id, score, level))
        conn.commit()
        print("Ойын аяқталды. Ұпай базаға сақталды.")

        # Аяқталу экранын көрсету
        screen.fill(BLACK)
        over_text = font.render("Game Over!", True, RED)
        info_text = font.render(f"Score: {score} | Level: {level}", True, WHITE)
        restart_text = font.render("R - restart | Q - quit", True, GG)
        screen.blit(over_text, ((WIDTH // 2) - 90, 70))
        screen.blit(info_text, ((WIDTH // 2) - 110, HEIGHT // 2 - 20))
        screen.blit(restart_text, (350, 370))
        pygame.display.flip()

        # Қайта бастау немесе шығу
        wait_for_choice = True
        while wait_for_choice:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    wait_for_choice = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        cur.execute("SELECT score, level FROM user_score WHERE user_id = %s ORDER BY saved_at DESC LIMIT 1", (user_id,))
                        row = cur.fetchone()
                        score = row[0] if row else 0
                        level = row[1] if row else 1
                        wait_for_choice = False
                    elif event.key == pygame.K_q:
                        running = False
                        wait_for_choice = False

    pygame.quit()  # Pygame-ді жабу

# Ойынды іске қосу
game()
cur.close()      # Курсорды жабу
conn.close()     # Дерекқорды жабу
