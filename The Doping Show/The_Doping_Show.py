import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
screen = pygame.display.set_mode((800, 600))

# Set the title of the window
pygame.display.set_caption("The Doping Game")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
