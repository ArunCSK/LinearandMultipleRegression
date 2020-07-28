import pygame
import time
import random

WHITE = (255,255,255)
GREY = (20,20,20)
BLACK = (0,0,0)
PURPLE = (100,0,100)
RED = (255,0,0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255 ,255 ,0)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 35
HEIGHT = 35

# SET rows and columns
ROWS = 29
COLUMNS = 52

# This sets the margin between each cell
MARGIN = 2

grid = []

# Draw the grid
for row in range(ROWS):
    for column in range(COLUMNS):
        color = BLACK
        pygame.draw.rect(screen,
                            color,
                            [(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN,
                            WIDTH ,
                            HEIGHT ])
        grid.append((column, row))                                            # add cell to grid list
pygame.display.flip()
pygame.display.update()

# setup maze variables
x = 0                    # x axis
y = 0                    # y axis
w = 35                   # width of cell
grid = []
visited = []
stack = []
solution = {}

def single_cell( x, y):
    pygame.draw.rect(screen, GREEN, ((MARGIN + WIDTH) * x + MARGIN, (MARGIN + HEIGHT) * y + MARGIN, WIDTH, HEIGHT), 0)          # draw a single width cell
    pygame.display.update()
    pygame.draw.rect(screen, BLUE, ((MARGIN + WIDTH) * x + MARGIN, (MARGIN + HEIGHT) * y + MARGIN, WIDTH, HEIGHT), 0)


def push_right(x, y):
    pygame.draw.rect(screen, GREEN, ((MARGIN + WIDTH) * x  + MARGIN , (MARGIN + HEIGHT) * y + MARGIN, WIDTH + WIDTH + MARGIN, HEIGHT), 0)
    pygame.display.update()
    pygame.draw.rect(screen, BLUE, ((MARGIN + WIDTH) * x  + MARGIN , (MARGIN + HEIGHT) * y + MARGIN, WIDTH + WIDTH + MARGIN, HEIGHT), 0)

def push_left(x, y):
    pygame.draw.rect(screen, GREEN, ((MARGIN + WIDTH) * (x - 1) + MARGIN, (MARGIN + HEIGHT) * y + MARGIN, WIDTH + WIDTH + MARGIN, HEIGHT), 0)
    pygame.display.update()
    pygame.draw.rect(screen, BLUE, ((MARGIN + WIDTH) * (x - 1) + MARGIN, (MARGIN + HEIGHT) * y + MARGIN, WIDTH + WIDTH + MARGIN, HEIGHT), 0)

def push_down(x, y):
    pygame.draw.rect(screen, GREEN, ((MARGIN + WIDTH) * x + MARGIN, (MARGIN + HEIGHT) * y + MARGIN, WIDTH, HEIGHT + HEIGHT + MARGIN), 0)
    pygame.display.update()
    pygame.draw.rect(screen, BLUE, ((MARGIN + WIDTH) * x + MARGIN, (MARGIN + HEIGHT) * y + MARGIN, WIDTH, HEIGHT + HEIGHT + MARGIN), 0)

def push_up(x, y):
    pygame.draw.rect(screen, GREEN, ((MARGIN + WIDTH) * x + MARGIN, (MARGIN + HEIGHT) * (y-1) + MARGIN, WIDTH, HEIGHT + HEIGHT + MARGIN), 0)         # draw a rectangle twice the width of the cell
    pygame.display.update()
    pygame.draw.rect(screen, BLUE, ((MARGIN + WIDTH) * x + MARGIN, (MARGIN + HEIGHT) * (y-1) + MARGIN, WIDTH, HEIGHT + HEIGHT + MARGIN), 0)                                            

def backtracking_cell(x, y):
    pygame.draw.rect(screen, GREEN, ((MARGIN + WIDTH) * x  + MARGIN, (MARGIN + HEIGHT) * y  + MARGIN, WIDTH, HEIGHT), 0)        # used to re-colour the path after single_cell
    pygame.display.update()
    pygame.draw.rect(screen, BLUE, ((MARGIN + WIDTH) * x  + MARGIN, (MARGIN + HEIGHT) * y  + MARGIN, WIDTH, HEIGHT), 0)                                       

def solution_cell(x,y):
    pygame.draw.rect(screen, PURPLE, ((MARGIN + WIDTH) * x+7 + MARGIN, (MARGIN + HEIGHT) * y+7 + MARGIN, 20, 20), 0)
    pygame.draw.rect(screen, RED, ((MARGIN + WIDTH) * x+15, (MARGIN + WIDTH) * y+15, 10, 10), 0)             # used to show the solution
    pygame.display.update()

def carve_out_maze(x,y):
    time.sleep(1)
    single_cell(x,y)
    stack.append((x,y))
    visited.append((x,y))

    while len(stack) > 0:
        #time.sleep(.10) 
        cell = []
        if (x+1,y) not in visited and x+1 in range(COLUMNS) and y in range(ROWS):
            cell.append("right")
            
        if (x - 1, y) not in visited and x-1 in range(COLUMNS) and y in range(ROWS):       # left cell available?
            cell.append("left")

        if (x , y + 1) not in visited and x in range(COLUMNS) and y+1 in range(ROWS):     # down cell available?
            cell.append("down")

        if (x, y - 1) not in visited and x in range(COLUMNS) and y-1 in range(ROWS):      # up cell available?
            cell.append("up")

        if  len(cell)> 0 :
            cell_chosen = (random.choice(cell))

            if cell_chosen == "right":
                push_right(x,y)
                solution[( x + 1,  y)] = x, y                        # solution = dictionary key = new cell, other = current cell
                x = x + 1                                          # make this cell the current cell
                visited.append((x, y))                              # add to visited list
                stack.append((x, y))                                # place current cell on to stack
            elif cell_chosen == "left":
                push_left(x, y)
                solution[( x - 1, y)] = x, y
                x = x - 1
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "down":
                push_down(x, y)
                solution[( x , y + 1)] = x, y
                y = y + 1
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "up":
                push_up(x, y)
                solution[( x , y - 1)] = x, y
                y = y - 1
                visited.append((x, y))
                stack.append((x, y))
        else:
            x, y = stack.pop()                                    # if no cells are available pop one from the stack
            single_cell(x, y)                                     # use single_cell function to show backtracking image
            backtracking_cell(x, y)

def plot_route_back(x,y):
    solution_cell(x, y)                                          # solution list contains all the coordinates to route back to start
    while (x, y) != (0,0):                                     # loop until cell position == start position
        x, y = solution[x, y]                                    # "key value" now becomes the new key
        #print(x, y)
        solution_cell(x, y)                                      # animate route back
        #time.sleep(.010)

carve_out_maze(0,0)               # call build the maze  function
#print(solution)
plot_route_back(51, 28)         # call the plot solution function

# x, y = solution[51, 28]
# print((x, y))


#Pygame exit loop
running = True
while running:
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False