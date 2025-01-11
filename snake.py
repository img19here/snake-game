import pygame
import random

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

#set display screen
screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
pygame.display.set_caption('Snake')

#define game variables
cell_size = 10
direction = 1 #1 is up , 2 is right , 3 is down , 4 is left
update_snake = 0
food = [0,0]
new_food = True
new_piece = [0,0]

#create snake
#give x,y coordinates of snake initially
snake_pos = [[int(SCREEN_WIDTH/2),int(SCREEN_HEIGHT/2)]]
snake_pos.append([int(SCREEN_WIDTH/2),int(SCREEN_HEIGHT/2) + cell_size])
snake_pos.append([int(SCREEN_WIDTH/2),int(SCREEN_HEIGHT/2) + cell_size*2])
snake_pos.append([int(SCREEN_WIDTH/2),int(SCREEN_HEIGHT/2) + cell_size*3])






#define colors
bg = (255,200,150)
body_inner = (50,175,25)
body_outer = (100,100,200)
food_col = (200,50,50)
red = (255,0,0)

def draw_screen():
    screen.fill(bg)
    

#set loop for game 
run = True
while run:
    
    draw_screen()
    
    #iterate through events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 3:
                direction = 1
            if event.key == pygame.K_RIGHT and direction != 4:
                direction = 2
            if event.key == pygame.K_DOWN and direction !=1:
                direction = 3
            if event.key == pygame.K_LEFT and direction != 2:
                direction = 4
     
    if new_food == True:
        new_food = False
        food [0] = cell_size * random.randint(0,int((SCREEN_WIDTH/cell_size) - 1)) 
        food [1] = cell_size * random.randint(0,int((SCREEN_HEIGHT/cell_size) - 1))            
    
    #draw food 
    pygame.draw.rect(screen,food_col,(food[0],food[1],cell_size,cell_size))
    
    
    #check if food is eaten
    if snake_pos[0] == food:
        new_food = True
        #create new piece
        new_piece = list(snake_pos[-1])
        if direction ==1:
            new_piece[1] += cell_size
        if direction ==3:
            new_piece[1] -= cell_size
        if direction ==2:
            new_piece[0] -= cell_size
        if direction ==4:
            new_piece[0] += cell_size
           
        #attach new piece to snake
        snake_pos.append(new_piece)
        
     
    if update_snake > 99:
        update_snake = 0
        snake_pos = snake_pos[-1:] + snake_pos[:-1]
        #heading up
        if direction == 1:
            snake_pos[0][0] = snake_pos[1][0]
            snake_pos[0][1] = snake_pos[1][1] - cell_size
        if direction == 3:
            snake_pos[0][0] = snake_pos[1][0]
            snake_pos[0][1] = snake_pos[1][1] + cell_size
        if direction == 2:
            snake_pos[0][1] = snake_pos[1][1]
            snake_pos[0][0] = snake_pos[1][0] + cell_size
        if direction == 4:
            snake_pos[0][1] = snake_pos[1][1]
            snake_pos[0][0] = snake_pos[1][0] - cell_size
        

    # draw snake
    head = 1
    for x in snake_pos:
        if head == 0:
            pygame.draw.rect(screen,body_outer,(x[0],x[1],cell_size,cell_size))
            pygame.draw.rect(screen,body_inner,(x[0]+1,x[1]+1,cell_size-2,cell_size-2))
        if head == 1:
            pygame.draw.rect(screen,body_outer,(x[0],x[1],cell_size,cell_size))
            pygame.draw.rect(screen,red,(x[0]+1,x[1]+1,cell_size-2,cell_size-2))
            head = 0


    #To update display screen during writing code            
    pygame.display.update()
    update_snake += 1
#end pygame
pygame.quit()
    

