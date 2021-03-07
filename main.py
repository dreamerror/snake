import pygame
import random

pygame.init()


sound_game_over = pygame.mixer.Sound('You_Died.wav')

height = 400
width = 300
snake_size = 10
snake_speed = 15

screen = pygame.display.set_mode((height, width))  # создание игрового экрана
# pygame.display.update()
pygame.display.set_caption('Snake GOTY Edition')  # заголовок окна

green = (0, 255, 0)
white = (0, 0, 0)
red = (255, 0, 0)
cyan = (0, 255, 255)
yellow = (255, 255, 102)

font_style = pygame.font.Font('Lobster.ttf', 20)
score_font = pygame.font.Font('Lobster.ttf', 10)

time = pygame.time.Clock()


def screen_text(text: str, color: tuple) -> None:
    hght = height // 3
    wdth = width // 3
    for seq in text.split('\n'):
        msg = font_style.render(seq, True, color)
        screen.blit(msg, [hght, wdth])
        wdth += 20


def draw_full_snake(snake_blocks):
    for cord in snake_blocks:
        pygame.draw.rect(screen, green, [cord[0], cord[1], snake_size, snake_size])


def print_score(score):
    value = font_style.render(f'Score: {score}', True, yellow)
    screen.blit(value, [0, 0])


def game():
    pygame.mixer.music.load('Nyan_Cat.wav')
    pygame.mixer.music.play(-1)

    game_closed = False
    game_over = False

    x = height // 2
    y = width // 2

    x_delta = 0
    y_delta = 0

    snake_blocks = []
    snake_len = 1

    food_x = round(random.randrange(0, height - snake_size) / float(snake_size)) * float(snake_size)
    food_y = round(random.randrange(0, width - snake_size) / float(snake_size)) * float(snake_size)

    while not game_over:

        while game_closed:
            pygame.mixer.music.pause()
            sound_game_over.play()
            screen.fill(white)
            screen_text('You lost! \n P — Play again \n Q — Quit', red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == ord('q'):
                        game_over = True
                        game_closed = False
                    if event.key == ord('p'):
                        game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_closed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    if not x_delta:
                        x_delta = -snake_size
                        y_delta = 0
                elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                    if not x_delta:
                        x_delta = snake_size
                        y_delta = 0
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    if not y_delta:
                        x_delta = 0
                        y_delta = -snake_size
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    if not y_delta:
                        x_delta = 0
                        y_delta = snake_size
        if y >= width:
            y = 0
        if y < 0:
            y = width
        if x >= height:
            x = 0
        if x < 0:
            x = height

        x += x_delta
        y += y_delta
        screen.fill(white)
        pygame.draw.rect(screen, red, [food_x, food_y, snake_size, snake_size])
        new_snake_block = list()
        new_snake_block.append(x)
        new_snake_block.append(y)
        snake_blocks.append(new_snake_block)

        if len(snake_blocks) > snake_len:
            snake_blocks.remove(snake_blocks[0])

        for t in snake_blocks[:-1]:
            if t == new_snake_block:
                game_closed = True

        draw_full_snake(snake_blocks)
        print_score(snake_len-1)
        pygame.display.update()

        if x == food_x and y == food_y:
            snake_len += 1
            print('nyam', f'score = {snake_len-1}')
            food_x = round(random.randrange(0, height - snake_size) / float(snake_size)) * float(snake_size)
            food_y = round(random.randrange(0, width - snake_size) / float(snake_size)) * float(snake_size)

        time.tick(snake_speed)

    pygame.quit()
    quit()


game()
