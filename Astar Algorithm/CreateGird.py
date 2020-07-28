"""
 Example program to show using an array to back a grid on-screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame
import time
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255 ,255 ,0)

COLORS = [WHITE,GREEN,RED,YELLOW]

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 40
HEIGHT = 40
ROWS = 14
COLUMNS = 25
# This sets the margin between each cell
MARGIN = 3
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(ROWS):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(COLUMNS):
        grid[row].append(0)  # Append a cell
    
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
#grid[1][5] = 1
#grid[len(grid)-2][len(grid[0])-5] = 1
#print(grid)
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [1080, 610]
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
 
# Set title of screen
pygame.display.set_caption("Array Backed Grid")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


display = True
font = pygame.font.Font(None, 50)
text = font.render("_", True,BLUE)

# start display color grids
# while pygame.time.get_ticks() < 5000: # run the program for 5 seconds
#     # empty the screen
#     screen.fill(BLACK)

#     color = RED
#     for c in COLORS:
#         for row in range(14):
#             for column in range(25):
#                 color = WHITE
#                 pygame.draw.rect(screen,
#                                 c,
#                                 [(MARGIN + WIDTH) * column + MARGIN,
#                                 (MARGIN + HEIGHT) * row + MARGIN,
#                                 WIDTH,
#                                 HEIGHT])
#         pygame.time.wait(400)
#         pygame.display.update()        

#     # update the actual screen
#     pygame.display.flip()

#     # wait for half second
#     #pygame.time.wait(100)

# screen.fill(BLACK)
# pygame.display.update()
# pygame.time.wait(1000)

display = True

# Draw the grid
for row in range(14):
    for column in range(25):
        color = WHITE
        pygame.draw.rect(screen,
                            color,
                            [(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN,
                            WIDTH,
                            HEIGHT])
pygame.display.update()

# -------- Grid Cell Clicked -----------
# while not done:
#     for event in pygame.event.get():  # User did something
#         if event.type == pygame.QUIT:  # If user clicked close
#             done = True  # Flag that we are done so we exit this loop
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             # User clicks the mouse. Get the position
#             pos = pygame.mouse.get_pos()
#             # Change the x/y screen coordinates to grid coordinates
#             column = pos[0] // (WIDTH + MARGIN)
#             row = pos[1] // (HEIGHT + MARGIN)
#             # Set that location to one
#             grid[row][column] = 1
#             color = GREEN
#             pygame.draw.rect(screen,
#                             color,
#                             [(MARGIN + WIDTH) * column + MARGIN,
#                             (MARGIN + HEIGHT) * row + MARGIN,
#                             WIDTH,
#                             HEIGHT])
#             print("Click ", pos, "Grid coordinates: ", row, column)
#             pygame.display.update()
# pygame.QUIT

# setup maze variables
x = 0                    # x axis
y = 0                    # y axis
w = 4                   # width of cell
visited = []
stack = []
solution = {}

def single_cell( x, y):
    #pygame.draw.rect(screen, GREEN, (x +w, y +w, 38, 38), 0)          # draw a single width cell
    pygame.draw.rect(screen,
                                GREEN,
                                [(MARGIN + WIDTH) * x + MARGIN,
                                (MARGIN + HEIGHT) * y + MARGIN,
                                WIDTH,
                                HEIGHT])
    pygame.display.update()

def push_right(x, y):
    #pygame.draw.rect(screen, BLUE, (x +1, y +1, 80, 40), 0)
    pygame.draw.rect(screen,
                            BLUE,
                            [(MARGIN + WIDTH) * x + MARGIN,
                            (MARGIN + HEIGHT) * y + MARGIN ,
                            WIDTH + WIDTH + MARGIN,
                            HEIGHT])
    pygame.display.update()

def push_left(x, y):
    #pygame.draw.rect(screen, BLUE, (x - w +1, y +1, 80, 38), 0)
    pygame.draw.rect(screen,
                            BLUE,
                            [(MARGIN + WIDTH) * x + MARGIN,
                            (MARGIN + HEIGHT) * y + MARGIN,
                            WIDTH - WIDTH - MARGIN,
                            HEIGHT])
    pygame.display.update()

def push_down(x, y):
    #pygame.draw.rect(screen, BLUE, (x +  1, y + 1, 38, 80), 0)
    pygame.draw.rect(screen,
                            BLUE,
                            [(MARGIN + WIDTH) * x + MARGIN,
                            (MARGIN + HEIGHT) * y + MARGIN,
                            WIDTH,
                            HEIGHT + HEIGHT + MARGIN])
    pygame.display.update()

def push_up(x, y):
    #pygame.draw.rect(screen, BLUE, (x + 1, y - w + 1, 38, 80), 0)         # draw a rectangle twice the width of the cell
    pygame.draw.rect(screen,
                            BLUE,
                            [(MARGIN + WIDTH) * x + MARGIN,
                            (MARGIN + HEIGHT) * y + MARGIN,
                            WIDTH,
                            HEIGHT - HEIGHT - MARGIN])
    pygame.display.update()                                              # to animate the wall being removed

def backtracking_cell(x, y):
    #pygame.draw.rect(screen, BLUE, (x +1, y +1, 38, 38), 0)        # used to re-colour the path after single_cell
    pygame.draw.rect(screen,
                            BLUE,
                            [(MARGIN + WIDTH) * x + MARGIN,
                            (MARGIN + HEIGHT) * y + MARGIN,
                            WIDTH,
                            HEIGHT])
    pygame.display.update()  

def solution_cell(x,y):
    #pygame.draw.rect(screen, YELLOW, (x+8, y+8, 5, 5), 0)             # used to show the solution
    pygame.draw.rect(screen,
                            YELLOW,
                            [(MARGIN + WIDTH) * x + MARGIN,
                            (MARGIN + HEIGHT) * y + MARGIN,
                            WIDTH,
                            HEIGHT])
    pygame.display.update()                                        # has visited cell

def Create_Maze(x,y):
    single_cell(x,y)
    stack.append((x,y))
    visited.append((x,y))

    while len(stack) > 0:
        time.sleep(.010) 
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
                solution[(x + 1, y)] = x, y                        # solution = dictionary key = new cell, other = current cell
                x = x + 1                                          # make this cell the current cell
                visited.append((x, y))                              # add to visited list
                stack.append((x, y))                                # place current cell on to stack
            elif cell_chosen == "left":
                push_left(x, y)
                solution[(x - 1, y)] = x, y
                x = x - 1
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "down":
                push_down(x, y)
                solution[(x , y + 1)] = x, y
                y = y + 1
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "up":
                push_up(x, y)
                solution[(x , y - 1)] = x, y
                y = y - 1
                visited.append((x, y))
                stack.append((x, y))
        else:
            x, y = stack.pop()                                    # if no cells are available pop one from the stack
            single_cell(x, y)                                     # use single_cell function to show backtracking image
            backtracking_cell(x, y)
    
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

def plot_route_back(x,y):
    solution_cell(x, y)                                          # solution list contains all the coordinates to route back to start
    while (x, y) != (0,0):                                     # loop until cell position == start position
        x, y = solution[x, y]                                    # "key value" now becomes the new key
        solution_cell(x, y)                                      # animate route back
        time.sleep(.010)

Create_Maze(0,0)   
plot_route_back(13, 24)         # call the plot solution function           
 # ##### pygame loop #######
running = True
while running:
    # keep running at the at the right speed
    clock.tick(30)
    # process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

