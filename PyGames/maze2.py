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

size = (1200,700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Maze Generator")

done = False
clock = pygame.time.Clock()

width = 25
cols = int(size[0] / width)
rows = int(size[1] / width)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 200
HEIGHT = 200
# This sets the margin between each cell
MARGIN = 3

ROWS = 20
COLUMNS = 35

# pygame.draw.rect(screen, RED, [100 , 100, 200 ,200])
# pygame.draw.rect(screen, WHITE, [300, 100, 200 ,200])
# pygame.draw.rect(screen, WHITE, [100, 300, 200 ,200])
# pygame.draw.rect(screen, BLUE, [300, 300, 200 ,200])


#MOVE DOWN
pygame.draw.rect(screen,RED,[(MARGIN + WIDTH) * 0 + MARGIN , 
                             (MARGIN + HEIGHT) * 0 + MARGIN ,
                             WIDTH + MARGIN , 
                             HEIGHT + MARGIN])
#TOP
pygame.draw.rect(screen,BLUE,[(MARGIN + WIDTH) * 0 + MARGIN , 
                              (MARGIN + HEIGHT) * 0 + MARGIN ,
                              WIDTH  , 
                              MARGIN ])
#LEFT
pygame.draw.rect(screen,BLUE,[(MARGIN + WIDTH) * 0 + MARGIN , 
                              (MARGIN + HEIGHT) * 0 + MARGIN ,
                              MARGIN, 
                              HEIGHT + MARGIN])
#RIGHT
pygame.draw.rect(screen,BLUE,[(MARGIN + WIDTH) * 0  + WIDTH + MARGIN, 
                              (WIDTH + MARGIN) * 0 + MARGIN,
                              MARGIN , 
                              HEIGHT + MARGIN])     

#MOVE RIGHT
pygame.draw.rect(screen,RED,[(MARGIN + WIDTH) * 2 + MARGIN , 
                             (MARGIN + HEIGHT) * 0 + MARGIN ,
                             WIDTH + MARGIN , 
                             HEIGHT + MARGIN])     
#TOP              
pygame.draw.rect(screen,BLUE,[(MARGIN + WIDTH) * 2 + MARGIN , 
                              (MARGIN + HEIGHT) * 0 + MARGIN ,
                              WIDTH + MARGIN , 
                              MARGIN ])
#LEFT
pygame.draw.rect(screen,BLUE,[(MARGIN + WIDTH) * 2 + MARGIN , 
                              (MARGIN + HEIGHT) * 0 + MARGIN ,
                              MARGIN, 
                              HEIGHT + MARGIN])
#BOTTOM
pygame.draw.rect(screen,BLUE,[(MARGIN + WIDTH) * 2 + MARGIN , 
                              (MARGIN + HEIGHT) * 0 + MARGIN + WIDTH ,
                              WIDTH + MARGIN, 
                              MARGIN])

#MOVE UP
pygame.draw.rect(screen,RED,[(MARGIN + WIDTH) * 4 + MARGIN , 
                             (MARGIN + HEIGHT) * 0 + MARGIN ,
                             WIDTH + MARGIN , 
                             HEIGHT + MARGIN])   
#RIGHT
pygame.draw.rect(screen,BLUE,[(MARGIN + WIDTH) * 4  + WIDTH + MARGIN, 
                              (WIDTH + MARGIN) * 0 + MARGIN,
                              MARGIN , 
                              HEIGHT + MARGIN])  
#LEFT 
pygame.draw.rect(screen,BLUE,[(MARGIN + WIDTH) * 4 + MARGIN , 
                              (MARGIN + HEIGHT) * 0 + MARGIN ,
                              MARGIN, 
                              HEIGHT + MARGIN])
#BOTTOM
pygame.draw.rect(screen,BLUE,[(MARGIN + WIDTH) * 4 + MARGIN , 
                              (MARGIN + HEIGHT) * 0 + MARGIN + WIDTH ,
                              WIDTH + MARGIN, 
                              MARGIN])

#MOVE LEFT
pygame.draw.rect(screen,RED,[(MARGIN + WIDTH) * 1 + MARGIN , 
                             (MARGIN + HEIGHT) * 1 + MARGIN ,
                             WIDTH + MARGIN , 
                             HEIGHT + MARGIN])   
#RIGHT
pygame.draw.rect(screen,BLUE,[(MARGIN + WIDTH) * 1  + WIDTH + MARGIN, 
                              (WIDTH + MARGIN) * 1 + MARGIN,
                              MARGIN , 
                              HEIGHT + MARGIN])  
#TOP              
pygame.draw.rect(screen,BLUE,[(MARGIN + WIDTH) * 1 + MARGIN , 
                              (MARGIN + HEIGHT) * 1 + MARGIN ,
                              WIDTH + MARGIN , 
                              MARGIN ])
#BOTTOM
pygame.draw.rect(screen,BLUE,[(MARGIN + WIDTH) * 1 + MARGIN , 
                              (MARGIN + HEIGHT) * 1 + MARGIN + WIDTH ,
                              WIDTH + MARGIN, 
                              MARGIN])
# # Draw the grid
# for row in range(ROWS):
#     for column in range(COLUMNS):
#         color = WHITE
#         pygame.draw.rect(screen,
#                             color,
#                             [(MARGIN + WIDTH) * column + MARGIN,
#                             (MARGIN + HEIGHT) * row + MARGIN,
#                             WIDTH,
#                             HEIGHT])
# pygame.display.flip()
# pygame.display.update()

# for row in range(ROWS):
#     for column in range(COLUMNS):
#         color = BLUE
#         pygame.draw.line(screen,
#                             RED,
#                             (column * (WIDTH + MARGIN) , row * (WIDTH + MARGIN)) ,
#                             ( ( (WIDTH + MARGIN) + (column * (WIDTH + MARGIN))),
#                             (row * (WIDTH + MARGIN) )), 1)

# pygame.draw.line(screen,
#                             BLUE,
#                             (0  , 0 ) ,
#                             ( 1 + WIDTH,
#                             0), 3)                            
pygame.display.update()


running = True
while running:
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False  

