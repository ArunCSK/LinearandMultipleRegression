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
WIDTH = 30
HEIGHT = 30
# This sets the margin between each cell
MARGIN = 1

ROWS = 20
COLUMNS = 35

# Draw the grid
for row in range(ROWS):
    for column in range(COLUMNS):
        color = WHITE
        pygame.draw.rect(screen,
                            color,
                            [(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN,
                            WIDTH + MARGIN ,
                            HEIGHT + MARGIN ])
pygame.display.flip()
pygame.display.update()

done = False
current_cell = (0,0)
next_cell = (0,0)
visited_cells = []
next_cells = []
stack = []
walls = [True, True, True, True]
x = 0
y = 0
top = (0,0)
bottom = (0,0)
left = (0,0)
right = (0,0)
diagonal = (0,0)

while not done:

    time.sleep(0.005)
    y,x = current_cell
    visited_cells.append(current_cell)

    if y-1 >= 0:                #check top cell
        top = (y-1, x)
        if top not in visited_cells and top not in next_cells:
            next_cells.append(top)
    
    if x-1 >= 0 :              #check left cell
        left = (y, x-1)
        if left not in visited_cells and left not in next_cells:
            next_cells.append(left)
    
    if y+1 <= COLUMNS -1:        #check bottom cell  
        bottom = (y+1, x)
        if bottom not in visited_cells and bottom not in next_cells:
            next_cells.append(bottom)
    
    if x+1 <= ROWS -1:     #check right cell
        right = (y, x+1)
        if right not in visited_cells and right not in next_cells:
            next_cells.append(right)
    
    pygame.draw.rect(screen, BLUE,[(MARGIN + WIDTH) * y + MARGIN, (MARGIN + WIDTH) * x + MARGIN, WIDTH + MARGIN, HEIGHT + MARGIN])
    pygame.display.update()

    #print(next_cells)
    if len(next_cells) > 0:
        next_cell = random.choice(next_cells)
        y1,x1 = current_cell
        y2,x2 = next_cell
        x = int(x1) - int(x2)
        y = int(y1) - int(y2)
        if x == -1:
            #pygame.draw.rect(screen, BLUE,[(MARGIN + WIDTH) * y1 + MARGIN + MARGIN, (MARGIN + WIDTH) * x1 + MARGIN , WIDTH , HEIGHT ]) # current cell move right
            #TOP              
            pygame.draw.rect(screen, BLUE,[(MARGIN + WIDTH) * y1 + MARGIN, (MARGIN + WIDTH) * x1 + MARGIN, WIDTH + MARGIN, HEIGHT + MARGIN])
            pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1 + MARGIN , (MARGIN + HEIGHT) * x1 + MARGIN ,WIDTH + MARGIN , MARGIN ])
            #LEFT
            pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1 + MARGIN , (MARGIN + HEIGHT) * x1 + MARGIN ,MARGIN, HEIGHT + MARGIN])
            #BOTTOM
            pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1 + MARGIN , (MARGIN + HEIGHT) * x1 + MARGIN + WIDTH ,WIDTH + MARGIN, MARGIN])
            
            #pygame.draw.rect(screen, BLUE,[(MARGIN + WIDTH) * y2 , (MARGIN + WIDTH) * x2 + MARGIN, WIDTH, HEIGHT]) # update next cell left
            pygame.display.update()
        if x == 1:
            pygame.draw.rect(screen, BLUE,[(MARGIN + WIDTH) * y1 + MARGIN, (MARGIN + WIDTH) * x1 + MARGIN, WIDTH + MARGIN, HEIGHT + MARGIN])
            #pygame.draw.rect(screen, BLUE,[(MARGIN + WIDTH) * y1  , (MARGIN + WIDTH) * x1 + MARGIN , WIDTH , HEIGHT]) # current cell move left
            #RIGHT
            pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1  + WIDTH + MARGIN, (WIDTH + MARGIN) * x1 + MARGIN,MARGIN , HEIGHT + MARGIN])  
            #TOP              
            pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1 + MARGIN , (MARGIN + HEIGHT) * x1 + MARGIN ,WIDTH + MARGIN , MARGIN ])
            #BOTTOM
            pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1 + MARGIN , (MARGIN + HEIGHT) * x1 + MARGIN + WIDTH ,WIDTH + MARGIN, MARGIN])
            #pygame.draw.rect(screen, BLUE,[(MARGIN + WIDTH) * y2 + MARGIN + MARGIN, (MARGIN + WIDTH) * x2 + MARGIN, WIDTH, HEIGHT]) # update next cell right
            pygame.display.update()
        if y == -1:
            pygame.draw.rect(screen, BLUE,[(MARGIN + WIDTH) * y1 + MARGIN, (MARGIN + WIDTH) * x1 + MARGIN, WIDTH + MARGIN, HEIGHT + MARGIN])
            #pygame.draw.rect(screen, BLUE,[(MARGIN + WIDTH) * y1 + MARGIN , (MARGIN + WIDTH) * x1 + MARGIN + MARGIN , WIDTH , HEIGHT]) # current cell move down
            #TOP
            pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1 + MARGIN , (MARGIN + HEIGHT) * x1 + MARGIN ,WIDTH  , MARGIN ])
            #LEFT
            pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1 + MARGIN , (MARGIN + HEIGHT) * x1 + MARGIN ,MARGIN, HEIGHT + MARGIN])
            #RIGHT
            pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1  + WIDTH + MARGIN, (WIDTH + MARGIN) * x1 + MARGIN,MARGIN , HEIGHT + MARGIN])
            #pygame.draw.rect(screen, BLUE,[(MARGIN + WIDTH) * y2 + MARGIN, (MARGIN + WIDTH) * x2 , WIDTH, HEIGHT + MARGIN]) # update next cell up
            pygame.display.update()
        if y == 1:
            pygame.draw.rect(screen, BLUE,[(MARGIN + WIDTH) * y1 + MARGIN, (MARGIN + WIDTH) * x1 + MARGIN, WIDTH + MARGIN, HEIGHT + MARGIN])
            #pygame.draw.rect(screen, BLUE,[(MARGIN + WIDTH) * y1 + MARGIN , (MARGIN + WIDTH) * x1   , WIDTH  , HEIGHT]) # current cell move up
            #RIGHT
            pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1  + WIDTH + MARGIN, (WIDTH + MARGIN) * x1 + MARGIN,MARGIN , HEIGHT + MARGIN])  
            #LEFT 
            pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1 + MARGIN , (MARGIN + HEIGHT) * x1 + MARGIN ,MARGIN, HEIGHT + MARGIN])
            #BOTTOM
            pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1 + MARGIN , (MARGIN + HEIGHT) * x1 + MARGIN + WIDTH ,WIDTH + MARGIN, MARGIN])
            #pygame.draw.rect(screen, BLUE,[(MARGIN + WIDTH) * y2 + MARGIN, (MARGIN + WIDTH) * x2 + MARGIN + MARGIN, WIDTH, HEIGHT]) # update next cell down
            pygame.display.update()
        current_cell = next_cell
        y,x = current_cell
        pygame.draw.rect(screen, RED,[(MARGIN + WIDTH) * y + MARGIN, (MARGIN + WIDTH) * x + MARGIN, WIDTH, HEIGHT])
        pygame.display.update()
        stack.append(current_cell)
        next_cells.clear()
    elif len(stack) > 0:
        next_cell = stack.pop()
        y1,x1 = current_cell
        y2, x2 = next_cell
        x = int(x1) - int(x2)
        y = int(y1) - int(y2)
        # if x == -1:
        #     #pygame.draw.rect(screen, BLUE,[(MARGIN + WIDTH) * y1 + MARGIN + MARGIN, (MARGIN + WIDTH) * x1 + MARGIN , WIDTH , HEIGHT ]) # current cell move right
        #     #TOP              
        #     pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1 + MARGIN , (MARGIN + HEIGHT) * x1 + MARGIN ,WIDTH + MARGIN , MARGIN ])
        #     #LEFT
        #     pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1 + MARGIN , (MARGIN + HEIGHT) * x1 + MARGIN ,MARGIN, HEIGHT + MARGIN])
        #     #BOTTOM
        #     pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1 + MARGIN , (MARGIN + HEIGHT) * x1 + MARGIN + WIDTH ,WIDTH + MARGIN, MARGIN])
            
        #     #pygame.draw.rect(screen, BLUE,[(MARGIN + WIDTH) * y2 , (MARGIN + WIDTH) * x2 + MARGIN, WIDTH, HEIGHT]) # update next cell left
        #     pygame.display.update()
        # if x == 1:
        #     #pygame.draw.rect(screen, BLUE,[(MARGIN + WIDTH) * y1 , (MARGIN + WIDTH) * x1 + MARGIN , WIDTH , HEIGHT]) # current cell move left
        #     #RIGHT
        #     pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1  + WIDTH + MARGIN, (WIDTH + MARGIN) * x1 + MARGIN,MARGIN , HEIGHT + MARGIN])  
        #     #TOP              
        #     pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1 + MARGIN , (MARGIN + HEIGHT) * x1 + MARGIN ,WIDTH + MARGIN , MARGIN ])
        #     #BOTTOM
        #     pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1 + MARGIN , (MARGIN + HEIGHT) * x1 + MARGIN + WIDTH ,WIDTH + MARGIN, MARGIN])
        #     #pygame.draw.rect(screen, BLUE,[(MARGIN + WIDTH) * y2 + MARGIN + MARGIN, (MARGIN + WIDTH) * x2 + MARGIN, WIDTH, HEIGHT]) # update next cell right
        #     pygame.display.update()
        # if y == -1:
        #     #pygame.draw.rect(screen, BLUE,[(MARGIN + WIDTH) * y1 + MARGIN , (MARGIN + WIDTH) * x1 + MARGIN + MARGIN , WIDTH , HEIGHT]) # current cell move down
        #     #TOP
        #     pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1 + MARGIN , (MARGIN + HEIGHT) * x1 + MARGIN ,WIDTH  , MARGIN ])
        #     #LEFT
        #     pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1 + MARGIN , (MARGIN + HEIGHT) * x1 + MARGIN ,MARGIN, HEIGHT + MARGIN])
        #     #RIGHT
        #     pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1  + WIDTH + MARGIN, (WIDTH + MARGIN) * x1 + MARGIN,MARGIN , HEIGHT + MARGIN])
        #     #pygame.draw.rect(screen, BLUE,[(MARGIN + WIDTH) * y2 + MARGIN, (MARGIN + WIDTH) * x2 , WIDTH, HEIGHT + MARGIN]) # update next cell up
        #     pygame.display.update()
        # if y == 1:
        #     #pygame.draw.rect(screen, BLUE,[(MARGIN + WIDTH) * y1 + MARGIN , (MARGIN + WIDTH) * x1 , WIDTH  , HEIGHT]) # current cell move up
        #     #RIGHT
        #     pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1  + WIDTH + MARGIN, (WIDTH + MARGIN) * x1 + MARGIN,MARGIN , HEIGHT + MARGIN])  
        #     #LEFT 
        #     pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1 + MARGIN , (MARGIN + HEIGHT) * x1 + MARGIN ,MARGIN, HEIGHT + MARGIN])
        #     #BOTTOM
        #     pygame.draw.rect(screen,BLACK,[(MARGIN + WIDTH) * y1 + MARGIN , (MARGIN + HEIGHT) * x1 + MARGIN + WIDTH ,WIDTH + MARGIN, MARGIN])
        #     #pygame.draw.rect(screen, BLUE,[(MARGIN + WIDTH) * y2 + MARGIN, (MARGIN + WIDTH) * x2 + MARGIN + MARGIN, WIDTH, HEIGHT]) # update next cell down
        #     pygame.display.update()
        current_cell = next_cell
        y,x = current_cell
        pygame.draw.rect(screen, RED,[(MARGIN + WIDTH) * y2 + MARGIN, (MARGIN + WIDTH) * x2 + MARGIN, WIDTH, HEIGHT])
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

 # ##### pygame loop #######
running = True
while running:
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False  