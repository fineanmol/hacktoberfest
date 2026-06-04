## LANGUAGE: Python
## ENV: Python
## AUTHOR: Sarvesh Pandit
## GITHUB: https://github.com/crystaxit 

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 200))
pygame.display.set_caption("Hello, World!")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load a font
font = pygame.font.Font(None, 36)

# Create a text surface
text = font.render("Hello, World! From Sarvesh Pandit", True, WHITE)

# Initial position of the text
text_x = 100
text_y = 100

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Display the text
    screen.blit(text, (text_x, text_y))

    # Update the display
    pygame.display.flip()

    # Move the text
    text_x += 1
    if text_x > 300:
        text_x = 100

    pygame.time.delay(10)  # Delay to control text speed

# Quit Pygame
pygame.quit()

# Exit the program
sys.exit()
