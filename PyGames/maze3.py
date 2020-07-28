import random
import pygame
import time

pygame.init()

WHITE = (255,255,255)
GREY = (20,20,20)
BLACK = (0,0,0)
PURPLE = (100,0,100)
RED = (255,0,0)
BLUE = (0, 0, 255)

# Set diplay full screen
windowWidth = None
windowHeight = None
info = pygame.display.Info()
windowWidth = info.current_w
windowHeight = info.current_h
screen = pygame.display.set_mode((windowWidth, windowHeight), pygame.FULLSCREEN)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 40
HEIGHT = 40

# SET rows and columns
ROWS = 25
COLUMNS = 45

# This sets the margin between each cell
MARGIN = 1

# Draw the grid
for row in range(ROWS):
    for column in range(COLUMNS):
        color = WHITE
        pygame.draw.rect(screen,
                            color,
                            [(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN,
                            WIDTH ,
                            HEIGHT ])
pygame.display.flip()
pygame.display.update()

#Initialize
done = False
current_cell = (0,0)
x = 0
y = 0

while not done:

    for columns in range(COLUMNS):
        for rows in range(ROWS):
            for r in range(rows):
                pygame.draw.rect(screen,BLUE,[(MARGIN + WIDTH) * columns + MARGIN, (MARGIN + HEIGHT) * r + MARGIN, WIDTH, HEIGHT])
                pygame.display.update()
            time.sleep(0.005)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.display.quit()
                running = False

 # ##### pygame loop #######
running = True
while running:
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.display.quit()
                running = False  