# Project Initialized on 16 October 2023
# Main file for a snake game using pygame
# JMJ

import pygame
import sys
from comps import colors

# https://www.pygame.org/docs/
# Initialize pygame
pygame.init()
#Create a screen
screen = pygame.display.set_mode((600,600))
#Draw out the screen
width = 50
height = 50


#Set a clock
clock = pygame.time.Clock()
#Set a boolean variable for whether the app is running or not
running = True

snake_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
snake_head = pygame.Rect(snake_pos.x - 10, snake_pos.y - 10, 20, 20)
speed = 10

#Start the loop for the game
while running:
    #Start with an event listening loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Add bg color
    screen.fill(colors.BACKGROUND_COLOR)
    # Add play space

    # Render here...

    pygame.draw.rect(screen, colors.GREEN, snake_head)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake_pos.y -= speed
    if keys[pygame.K_s]:
        snake_pos.y += speed
    if keys[pygame.K_a]:
        snake_pos.x -= speed
    if keys[pygame.K_d]:
        snake_pos.x += speed
    snake_head.update(snake_pos.x, snake_pos.y, 20, 20)


    # .flip() to display work on screen
    pygame.display.flip()

    # Determines framerate
    clock.tick(20)



#Once the game loop has ended, quit
pygame.quit()
    