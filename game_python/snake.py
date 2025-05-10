import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Screen dimensions
WIDTH = 600
HEIGHT = 400

# Snake settings
SNAKE_BLOCK = 10
SNAKE_SPEED = 10

# Initialize game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 30)

def show_splash_screen():
    screen.fill(BLUE)
    splash_font = pygame.font.SysFont("comicsansms", 40, bold=True)
    text = splash_font.render("Developed by ACT91", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(2000)

def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, BLACK, [block[0], block[1], snake_block, snake_block], border_radius=4)
        pygame.draw.rect(screen, GREEN, [block[0]+2, block[1]+2, snake_block-4, snake_block-4], border_radius=4)

def draw_food(x, y, snake_block):
    pygame.draw.ellipse(screen, RED, [x, y, snake_block, snake_block])
    pygame.draw.ellipse(screen, WHITE, [x+2, y+2, snake_block-4, snake_block-4])

def draw_border():
    border_thickness = 4
    pygame.draw.rect(screen, BLACK, [0, 0, WIDTH, HEIGHT], border_thickness)

def display_score(score):
    value = score_font.render(f"Score: {score}", True, WHITE)
    screen.blit(value, [10, 10])

def display_message(msg, color, x, y):
    message = font_style.render(msg, True, color)
    screen.blit(message, [x, y])

def draw_thorns():
    thorn_size = 8
    # Draw thorns on top and bottom walls
    for x in range(0, WIDTH, 20):
        # Top wall thorns
        pygame.draw.polygon(screen, RED, [
            (x, 0),
            (x + 10, 10),
            (x + 20, 0)
        ])
        # Bottom wall thorns
        pygame.draw.polygon(screen, RED, [
            (x, HEIGHT),
            (x + 10, HEIGHT - 10),
            (x + 20, HEIGHT)
        ])
    
    # Draw thorns on left and right walls
    for y in range(0, HEIGHT, 20):
        # Left wall thorns
        pygame.draw.polygon(screen, RED, [
            (0, y),
            (10, y + 10),
            (0, y + 20)
        ])
        # Right wall thorns
        pygame.draw.polygon(screen, RED, [
            (WIDTH, y),
            (WIDTH - 10, y + 10),
            (WIDTH, y + 20)
        ])

def game_loop():
    game_over = False
    game_close = False
    
    x = WIDTH / 2
    y = HEIGHT / 2
    x_change = 0
    y_change = 0
    
    snake_list = []
    length_of_snake = 1
    
    food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
    
    while not game_over:
        while game_close:
            screen.fill(WHITE)
            display_message("Game Over! Press Q-Quit or C-Play Again", RED, WIDTH / 6, HEIGHT / 3)
            display_score(length_of_snake - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -SNAKE_BLOCK
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = SNAKE_BLOCK
                    x_change = 0
        
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True
        
        x += x_change
        y += y_change
        screen.fill(BLUE)
        draw_border()
        draw_thorns()
        draw_food(food_x, food_y, SNAKE_BLOCK)
        
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True
        
        draw_snake(SNAKE_BLOCK, snake_list)
        display_score(length_of_snake - 1)
        pygame.display.update()
        
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            length_of_snake += 1
        
        clock.tick(SNAKE_SPEED)
    
    pygame.quit()
    quit()

# Start the game
show_splash_screen()
game_loop()
