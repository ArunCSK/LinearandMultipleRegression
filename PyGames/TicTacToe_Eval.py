import pygame
import socket
import time
import os
from math import inf as infinity
from random import choice

os.environ['PyGames'] = "D://Arundev//py//MachineLearningAlgorithms//PyGames"
cross = pygame.image.load('D://Arundev//py/MachineLearningAlgorithms//PyGames//cross.jpg')
circle = pygame.image.load('D://Arundev//py/MachineLearningAlgorithms//PyGames//circle.jpg')

#set display
win = pygame.display.set_mode((550,550))
#set caption
pygame.display.set_caption("Tic-Tac-Toe")

#define color
blue=(0,0,255)
white = (255, 255, 225)
grey = (225,225,150)
black = (0, 0, 0)
red = (255, 0, 0)

HUMAN = -1
COMP = +1
# board = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0],
# ]

def message(msg,color):
    font_style = pygame.font.SysFont("comicsansms", 40)
    win.fill(black)
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [550/3, 550/3])
   

def main():
    pygame.init()

    board = [[0, 0, 0],  
             [0, 0, 0],  
             [0, 0, 0]]  
    

    
    #Display each cells
    #first row
    first = pygame.draw.rect(win, white,(25,25,160,160))
    second = pygame.draw.rect(win, white,(200,25,160,160))
    third = pygame.draw.rect(win, white,(375,25,160,160))

    #second row
    fourth = pygame.draw.rect(win, white,(25,200,160,160))
    fifth  = pygame.draw.rect(win,white,(200,200,160,160))
    six = pygame.draw.rect(win,white,(375,200,160,160))

    #third row
    seventh = pygame.draw.rect(win,white,(25,375,160,160))
    eighth = pygame.draw.rect(win,white,(200,375,160,160))
    ninth = pygame.draw.rect(win,white,(375,375,160,160))

    pygame.display.update()
    time.sleep(1)
    run = True
    isMax = True

    #while run:
    while len(empty_cells(board)) > 0 and not game_over(board):
        board = PlayGame_HumanMove(run,first,second,third,fourth,fifth,six,seventh,eighth,ninth,board)
        pygame.display.update()
        #time.sleep(1)   
        print("Human move",board)
        if(game_over(board)):
            time.sleep(1)
            message("You Won!!!", red)
            pygame.display.update()
            time.sleep(2)
            #print("Human wins!!!")
            break
        board = PlayGame_AIMove(board,first,second,third,fourth,fifth,six,seventh,eighth,ninth)
        pygame.display.update()
        #time.sleep(1)   
        print("AI Move:",board)
        if(game_over(board)):
            time.sleep(1)    
            message("AI Wins!!!", red)
            pygame.display.update()
            time.sleep(2)    
            #print("AI wins!!!")
            break
    if not wins(board, "O") and not wins(board, "X"):
        message("It's a Draw", red)
        time.sleep(3)
        pygame.display.update()
    pygame.time.delay(10)


def PlayGame_HumanMove(run,first,second,third,fourth,fifth,six,seventh,eighth,ninth,board):
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0
    c8 = 0
    c9 = 0
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            #Quit Game
            if event.type == pygame.QUIT:
                run = False
            #Mouse Hover
            # if first.collidepoint(pygame.mouse.get_pos()) and c1==0:
            #     first = pygame.draw.rect(win, grey,(25,25,160,160))
            #     pygame.draw.line(win,red,(50,50) ,(150,150),10)
            #     pygame.draw.line(win,red,(150,50) ,(50,150),10)
            #     pygame.display.update()
            # elif c1==0:
            #     first = pygame.draw.rect(win, white,(25,25,160,160))
            #     pygame.display.update()

            # if second.collidepoint(pygame.mouse.get_pos()) and c2==0:
            #     second = pygame.draw.rect(win, grey,(200,25,160,160))
            #     pygame.draw.line(win,red,(225,50) ,(325,150),10)
            #     pygame.draw.line(win,red,(325,50) ,(225,150),10)
            #     pygame.display.update()
            # elif c2==0:
            #     second = pygame.draw.rect(win, white,(200,25,160,160))
            #     pygame.display.update()
            
            # if third.collidepoint(pygame.mouse.get_pos()) and c3==0:
            #     third = pygame.draw.rect(win, grey,(375,25,160,160))
            #     pygame.draw.line(win,red,(400,50) ,(500,150),10)
            #     pygame.draw.line(win,red,(500,50) ,(400,150),10)
            #     pygame.display.update()
            # elif c3==0:
            #     third = pygame.draw.rect(win, white,(375,25,160,160))
            #     pygame.display.update()

            # if fourth.collidepoint(pygame.mouse.get_pos()) and c4==0:
            #     fourth = pygame.draw.rect(win, grey,(25,200,160,160))
            #     pygame.draw.line(win,red,(50,225) ,(150,325),10)
            #     pygame.draw.line(win,red,(50,325) ,(150,225),10)
            #     pygame.display.update()
            # elif c4==0:
            #     fourth = pygame.draw.rect(win, white,(25,200,160,160))
            #     pygame.display.update()

            # if fifth.collidepoint(pygame.mouse.get_pos()) and c5==0:
            #     fifth = pygame.draw.rect(win, grey,(200,200,160,160))
            #     pygame.draw.line(win,red,(225,225) ,(325,325),10)
            #     pygame.draw.line(win,red,(325,225) ,(225,325),10)
            #     pygame.display.update()
            # elif c5==0:
            #     fifth = pygame.draw.rect(win, white,(200,200,160,160))
            #     pygame.display.update()
            
            # if six.collidepoint(pygame.mouse.get_pos()) and c6==0:
            #     six = pygame.draw.rect(win, grey,(375,200,160,160))
            #     pygame.draw.line(win,red,(400,225) ,(500,325),10)
            #     pygame.draw.line(win,red,(500,225) ,(400,325),10)
            #     pygame.display.update()
            # elif c6==0:
            #     six = pygame.draw.rect(win, white,(375,200,160,160))
            #     pygame.display.update()
            
            # if seventh.collidepoint(pygame.mouse.get_pos()) and c7==0:
            #     seventh = pygame.draw.rect(win, grey,(25,375,160,160))
            #     pygame.draw.line(win,red,(50,400) ,(150,500),10)
            #     pygame.draw.line(win,red,(150,400) ,(50,500),10)
            #     pygame.display.update()
            # elif c7==0:
            #     seventh = pygame.draw.rect(win, white,(25,375,160,160))
            #     pygame.display.update()

            # if eighth.collidepoint(pygame.mouse.get_pos()) and c8==0:
            #     eighth = pygame.draw.rect(win, grey,(200,375,160,160))
            #     pygame.draw.line(win,red,(225,400) ,(325,500),10)
            #     pygame.draw.line(win,red,(325,400) ,(225,500),10)
            #     pygame.display.update()
            # elif c8==0:
            #     eighth = pygame.draw.rect(win, white,(200,375,160,160))
            #     pygame.display.update()     

            # if ninth.collidepoint(pygame.mouse.get_pos()) and c9==0:
            #     ninth = pygame.draw.rect(win, grey,(375,375,160,160))
            #     pygame.draw.line(win,red,(400,400) ,(500,500),10)
            #     pygame.draw.line(win,red,(500,400) ,(400,500),10)
            #     pygame.display.update()
            # elif c9==0:
            #     ninth = pygame.draw.rect(win, white,(375,375,160,160))
            #     pygame.display.update()           

            #Get Position and display image on click
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                #print(pos)

                if first.collidepoint(pos):
                    first = pygame.draw.rect(win, white,(25,25,160,160))
                    win.blit(cross,[60,60])
                    c1=1
                    board[0][0] = "X"
                    #print(board)
                    return board
                if second.collidepoint(pos):
                    second = pygame.draw.rect(win, white,(200,25,160,160))
                    win.blit(cross,[230,60])
                    c2=1
                    board[0][1] = "X"
                    #print(board)
                    return board
                if third.collidepoint(pos):
                    third = pygame.draw.rect(win, white,(375,25,160,160))
                    win.blit(cross,[400,60])
                    c3=1
                    board[0][2] = "X"
                    #print(board)
                    return board
                if fourth.collidepoint(pos):
                    fourth = pygame.draw.rect(win, white,(25,200,160,160))
                    win.blit(cross,[60,225])
                    c4=1
                    board[1][0] = "X"
                    #print(board)
                    return board
                if fifth.collidepoint(pos):
                    fifth = pygame.draw.rect(win, white,(200,200,160,160))
                    win.blit(cross,[230,225])
                    c5=1
                    board[1][1] = "X"
                    #print(board)
                    return board
                if six.collidepoint(pos):
                    six = pygame.draw.rect(win, white,(375,200,160,160))
                    win.blit(cross,[400,225])
                    c6=1
                    board[1][2] = "X"
                    #print(board)
                    return board
                if seventh.collidepoint(pos):
                    seventh = pygame.draw.rect(win, white,(25,375,160,160))
                    win.blit(cross,[60,400])
                    c7=1
                    board[2][0] = "X"
                    print(board)
                    return board
                if eighth.collidepoint(pos):
                    eighth = pygame.draw.rect(win, white,(200,375,160,160))
                    win.blit(cross,[230,400])
                    c8=1
                    board[2][1] = "X"
                    #print(board)
                    return board
                if ninth.collidepoint(pos):
                    ninth = pygame.draw.rect(win, white,(375,375,160,160))
                    win.blit(cross,[400,400])
                    c9=1
                    board[2][2] = "X"
                    #print(board)
                    return board

        pygame.display.update()
    pygame.QUIT()

#Check for empty cells
def empty_cells(board):
    cells = []

    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells

def PlayGame_AIMove(board,first,second,third,fourth,fifth,six,seventh,eighth,ninth):

    depth = len(empty_cells(board))

    if depth == 0 or game_over(board):
        return board

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, "O")
        x, y = move[0], move[1]
    

    if(x==0 and y==0):
        first = pygame.draw.rect(win, white,(25,25,160,160))
        win.blit(circle,[60,60])
    elif(x==0 and y==1):
        second = pygame.draw.rect(win, white,(200,25,160,160))
        win.blit(circle,[230,60])
    elif(x==0 and y==2):
        third = pygame.draw.rect(win, white,(375,25,160,160))
        win.blit(circle,[400,60])
    elif(x==1 and y==0):
        fourth = pygame.draw.rect(win, white,(25,200,160,160))
        win.blit(circle,[60,225])
    elif(x==1 and y==1):
        fifth = pygame.draw.rect(win, white,(200,200,160,160))
        win.blit(circle,[230,225])
    elif(x==1 and y==2):
        six = pygame.draw.rect(win, white,(375,200,160,160))
        win.blit(circle,[400,225])
    elif(x==2 and y==0):
        seventh = pygame.draw.rect(win, white,(25,375,160,160))
        win.blit(circle,[60,400])
    elif(x==2 and y==1):
        eighth = pygame.draw.rect(win, white,(200,375,160,160))
        win.blit(circle,[230,400])
    elif(x==2 and y==2):
        ninth = pygame.draw.rect(win, white,(375,375,160,160))
        win.blit(circle,[400,400])

    board[x][y] = "O"
    return board

def evaluate(state):
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if wins(state, "O"):
        score = +1
    elif wins(state, "X"):
        score = -1
    else:
        score = 0

    return score

def minimax(state, depth, player):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == "O":
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        if player == "X":
           score = minimax(state, depth - 1, "O")
        else:
            score = minimax(state, depth - 1, "X")
        
        
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == "O":
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best

#Check winner
def game_over(board):
    return wins(board, "O") or wins(board, "X")


def wins(state, player):
    """
    This function tests if a specific player wins. Possibilities:
    * Three rows    [X X X] or [O O O]
    * Three cols    [X X X] or [O O O]
    * Two diagonals [X X X] or [O O O]
    :param state: the state of the current board
    :param player: a human or a computer
    :return: True if the player wins
    """
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
