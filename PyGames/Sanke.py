#py -m pip install -U pygame --user
#py -m pygame.examples.aliens
#pip install pygame
import pygame
import time
import random

pygame.init()

dis_width = 600
dis_height = 500

dis = pygame.display.set_mode((dis_width,dis_height))
#play_area = pygame.display.set_mode((dis_width-20,dis_height-50))
pygame.display.set_caption("Snake Game")

blue=(0,0,255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)




clock = pygame.time.Clock()
snake_speed=15

font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, blue)
    dis.blit(value, [20, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    if(msg == "Game Over!!!"):
        dis.blit(mesg, [dis_width/3, dis_height/3])
    else:
        dis.blit(mesg, [dis_width/8, dis_height/3])

def game_loop():
    game_over = False
    game_close = False  

    x1 = dis_width / 2
    y1 = dis_height / 2

    snake_block = 10

    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(20, 580) / 10.0) * 10.0
    foody = round(random.randrange(50, 480) / 10.0) * 10.0

    


    while not game_over:

        while game_close == True:
            dis.fill(black)
            
            message("You Lost! Press C-Play Again or Q-Quit", red)
 
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            print(event)
            if  event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10

        if x1 >= 580 or x1 < 20 or y1 >= 480 or y1 < 50:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        #Define Game Area
        pygame.draw.rect(dis, white, [dis_width-580, dis_height-450, dis_width-40, dis_height- 70])
        pygame.draw.rect(dis, black, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        #pygame.draw.rect(dis, blue, [x1,y1, snake_block,snake_block])
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()
        clock.tick(snake_speed)

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(20, 580) / 10.0) * 10.0
            foody = round(random.randrange(50, 470) / 10.0) * 10.0
            Length_of_snake += 1
    clock.tick(snake_speed)        

    message("Game Over!!!",red)
    pygame.display.update()
    time.sleep(1)
    pygame.quit()
#quit()

game_loop()