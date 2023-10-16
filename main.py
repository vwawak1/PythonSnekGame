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


#Start the loop for the game
while running:
    #Start with an event listening loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            print(event)

    # Add bg color
    screen.fill(colors.BACKGROUND_COLOR)

    # Render here...

    # .flip() to display work on screen
    pygame.display.flip()

    # Determines framerate
    clock.tick(60)



#Once the game loop has ended, quit
pygame.quit()
    