from logics_2048 import *
from database import cur, get_best, insert_res
import pygame
import sys
import json
import os

def draw_top_gamers():
    font_top = pygame.font.SysFont('arial', 20)
    font_gamer = pygame.font.SysFont('arial', 20)
    text_head = font_top.render(f"Best tryies", True, (0, 0, 255))
    screen.blit(text_head, (320, 5))
    for ind, gamer in enumerate(GAMERS_DB):
        name, score = gamer
        s = f"{ind + 1}. {name} - {score}"
        text_gamer = font_gamer.render(s, True, (0, 0, 255))
        screen.blit(text_gamer, (320, 25 + 20 * ind))
        print(ind, name, score)

def draw_interface(score, delta = 0):
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    font = pygame.font.SysFont('arial', 50)
    font_score = pygame.font.SysFont('arial', 50)
    font_delta = pygame.font.SysFont('arial', 25)
    text_score = font_score.render("Score : ", True, (0, 0, 255))
    text_score_value = font_score.render(f"{score}", True, (0, 0, 255))
    screen.blit(text_score, (20, 35))
    screen.blit(text_score_value, (200, 35))
    if delta > 0:
        text_delta = font_delta.render(f"+{delta}", True, (0, 0, 255))
        screen.blit(text_delta, (170, 25))
    pretty_print(mas)
    draw_top_gamers()           
    for row in range(BLOCKS):
        for col in range(BLOCKS):
            value = mas[row][col]
            text = font.render(f"{value}", True, (0,0,0))
            w = col * SIZE_BLOCK + MARGIN * (col + 1)
            h = row * SIZE_BLOCK + (row + 1) * MARGIN + TITLE_SIZE
            pygame.draw.rect(screen, COLORS[value], (w, h, SIZE_BLOCK, SIZE_BLOCK))  # Исправлено: SIZE_BLOCK вместо TITLE_SIZE
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = w + (SIZE_BLOCK - font_w) / 2
                text_y = h + (SIZE_BLOCK - font_h) / 2
                screen.blit(text, (text_x, text_y))

# Consts
BLOCKS = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK + (BLOCKS + 1) * MARGIN
TITLE_SIZE = 110
HEIGHT = BLOCKS * SIZE_BLOCK + (BLOCKS + 1) * MARGIN + TITLE_SIZE  # Исправлено: корректный расчёт высоты
TITLE_REC = pygame.Rect(0, 0, WIDTH, TITLE_SIZE)
GAMERS_DB = get_best()
score = 0

def init_const():
    global score, mas
    mas = [[0, 0, 0, 0] for _ in range(4)]
    score = 0
    empty = get_empty_list(mas)
    random.shuffle(empty)
    random_num1 = empty.pop()
    random_num2 = empty.pop()
    x1, y1 = get_index_from_number(random_num1)
    x2, y2 = get_index_from_number(random_num2)
    mas = insert_2_or_4(mas, x1, y1)
    mas = insert_2_or_4(mas, x2, y2)
    print(f'Completed element {random_num1}')    
    print(f'Completed element {random_num2}')
mas = None
score = None
USERNAME = None

#save
path = os.getcwd()
if 'data.txt' in os.listdir():
    with open('data.txt') as file:
        data = json.load(file)
        print(data)
        mas = data['mas']
        USERNAME = data['user'] 
        score = data['score']
    full_path = os.path.join(path, 'data.txt')
    os.remove(full_path)
else:
    init_const()
os.listdir(path)
print(get_empty_list(mas))
pretty_print(mas)

def save_game():
    data = {
        'user' : USERNAME,
        'score' : score,
        'mas' : mas
    }
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
# Colors
WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
BLACK = (0, 0, 0)
COLORS = {
    0: (130, 130, 130),
    2: (255, 255, 255),
    4: (255, 255, 128),
    8: (255, 255, 64),
    16: (255, 255, 32),
    32: (255, 255, 16),
    64: (255, 255, 8),
    128: (255, 15, 4),
    256: (255, 255, 2),
    512: (255, 255, 0),
    1024: (255, 255, 255)
}

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('2048')

def draw_intro():
    img2048 = pygame.image.load('img2048.png')
    font_welcome = pygame.font.SysFont('arial', 40)    
    text_welcome = font_welcome.render("Welcome!!!", True, WHITE)
    name = 'Fill your name' 
    is_find_name = False   
    while not is_find_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():                    
                    if name == 'Fill your name':
                        name = event.unicode
                    else:
                        name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(name) > 2:
                        global USERNAME
                        USERNAME = name
                        is_find_name = True
                        break   
        screen.fill((0,0,0))
        text_name = font_welcome.render(name, True, WHITE)
        rect_name = text_name.get_rect()
        rect_name.center = screen.get_rect().center

        screen.blit(pygame.transform.scale(img2048, (200, 200)), (10,10))
        screen.blit(text_welcome, (250, 75))
        screen.blit(text_name, rect_name)
        pygame.display.update()
    screen.fill((0,0,0))   

def draw_gameover():
    global USERNAME, mas, score, GAMERS_DB
    img2048 = pygame.image.load('img2048.png')
    font_gameover = pygame.font.SysFont('arial', 30)    
    text_gameover = font_gameover.render("Game Over!!!", True, WHITE)
    text_score = font_gameover.render(f"Your score is: {score}", True, WHITE)
    text_restart1 = font_gameover.render(f"Press Space to restart ", True, WHITE)
    text_restart2 = font_gameover.render(f"Press Enter for new name", True, WHITE) 
    best_score = GAMERS_DB[0][1] 
    if score > best_score:
        text = "New Record!"
    else:
        text = f"Record: {best_score}"
    text_record = font_gameover.render(text, True, WHITE)
    insert_res(USERNAME, score)
    GAMERS_DB = get_best()
    make_disicion = False
    while not make_disicion:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    make_disicion = True
                    init_const()                    
                elif event.key == pygame.K_RETURN:
                    
                    USERNAME = None
                    make_disicion = True
                    init_const()
        screen.fill(BLACK)   
        screen.fill((0,0,0))
        screen.blit(text_gameover, (250, 75))
        screen.blit(text_score, (30, 250))
        screen.blit(text_record, (30, 300))
        screen.blit(text_restart1, (30, 400))
        screen.blit(text_restart2, (30, 500))
        screen.blit(pygame.transform.scale(img2048, (200, 200)), (10,10))
        pygame.display.update()
    screen.fill(BLACK)

def game_loop():
    global score, mas
    draw_interface(score)
    pygame.display.update()
    is_mas_move = False    
    while is_zero_in_mas(mas) or can_move(mas):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game()
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                delta = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    mas, delta, is_mas_move = move_left(mas)                      
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    mas, delta, is_mas_move = move_right(mas)                    
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    mas, delta, is_mas_move = move_up(mas)                      
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    mas, delta, is_mas_move = move_down(mas)                     
                score += delta
                empty = get_empty_list(mas)
                random.shuffle(empty)
                if is_zero_in_mas(mas) and is_mas_move:
                    random_num = empty.pop()
                    x, y = get_index_from_number(random_num)
                    insert_2_or_4(mas, x, y)
                    print(f'Completed element {random_num}')
                    is_mas_move = False
                draw_interface(score, delta)            
                pygame.display.update()
        print(USERNAME)

while True:
    if USERNAME is None:
        draw_intro()
    game_loop()
    draw_gameover()
