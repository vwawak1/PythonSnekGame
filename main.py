# Project Initialized on 16 October 2023
# Main file for a snake game using pygame
# JMJ

import random
import pygame
import sys

# https://www.pygame.org/docs/
# Initialize pygame
pygame.init()

#Game variables
CELL_SIZE = 20
CELL_COUNT = 25
SCREEN_SIZE = CELL_COUNT * CELL_SIZE
BACKGROUND_COLOR = (68,93,72)
GREEN = (121,172,40)
RED = (255, 0, 0)

direction = "stop"
snack_check = False

#Create screen
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

# Methods

def draw_grid(screen, width, height, cell_size):
    for y in range(0,height, cell_size):
        for x in range(0, width, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, BACKGROUND_COLOR, rect, 1)


def movement():
    if direction == "up":
        snake_pos.y -= speed
    
    if direction == "down":
        snake_pos.y += speed
    
    if direction == "left":
        snake_pos.x -= speed
    
    if direction == "right":
        snake_pos.x += speed
    
    if direction == "stop":
        snake_pos.x = snake_pos.x
        snake_pos.y = snake_pos.y

    snake_head.update(snake_pos.x, snake_pos.y, 20, 20)

def generate_snack():
    print("Snack Generator!")
    x = random.randint(10, SCREEN_SIZE-10)
    y = random.randint(10, SCREEN_SIZE-10)
    return pygame.draw.rect(screen, RED, rect=(x, y, 15, 15))

def draw_snack(snack):
    pygame.draw.rect(screen, RED, snack)

#Set a clock
clock = pygame.time.Clock()
#Set a boolean variable for whether the app is running or not
running = True

snake_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
snake_head = pygame.Rect(snake_pos.x - 10, snake_pos.y - 10, 20, 20)
speed = 5



#Start the loop for the game
while running:
    #Start with an event listening loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Add bg color
    screen.fill(BACKGROUND_COLOR)
    # Add play space

    # Render here...

    #Begin frame by drawing the grid
    
    draw_grid(screen, SCREEN_SIZE, SCREEN_SIZE, CELL_SIZE)

    pygame.draw.rect(screen, GREEN, snake_head)

    #Get key inputs for controls
    keys = pygame.key.get_pressed()

    #Series of checks depending on the state of wasd
    if keys[pygame.K_w]:
        if direction != "down":
            direction = "up"
    if keys[pygame.K_s]:
        if direction != "up":
            direction = "down"
    if keys[pygame.K_a]:
        if direction != "right":
            direction = "left"
    if keys[pygame.K_d]:
        if direction != "left":
            direction = "right"

    if snack_check == False:
        snack = generate_snack()
        snack_check = True
    else:
        draw_snack(snack)
    
    movement()
    
    # .flip() to display work on screen
    pygame.display.flip()

    # Determines framerate
    clock.tick(60)


#Once the game loop has ended, quit
pygame.quit()
    