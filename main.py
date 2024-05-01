import sys
import numpy as np
import random
import pygame
import  math

white=(255,255,255)
black=(0,0,0)
red =(255,0,0)
yellow=(255,255,0)
row_count=6
col_count=7
human=0 #player
AI=1
human_ball=1
AI_ball= 2
win_length=4 #window_length
empty=0
def board():
    b=np.zeros((row_count,col_count))
    return b

def ball_placement(b,row,column,ball):
     b[row][column]=ball
def check_row(b,column):
    for i in range(row_count):
        if b[i][column]==0:
            return i
def is_valid_column(b,column):
    return b[row_count-1][column]==0

def flip_board(b):
    print(np.flip(b,0))
def check_win(b, ball):
    # Check horizontal wins
    for i in range(row_count):
        for j in range(col_count - 3):
            if b[i][j] == ball and b[i][j + 1] == ball and b[i][j + 2] == ball and b[i][j + 3] == ball:
                return True

    # Check vertical wins
    for i in range(row_count - 3):
        for j in range(col_count):
            if b[i][j] == ball and b[i + 1][j] == ball and b[i + 2][j] == ball and b[i + 3][j] == ball:
                return True

    # Check diagonal wins (positive slope)
    for i in range(row_count - 3):
        for j in range(col_count - 3):
            if b[i][j] == ball and b[i + 1][j + 1] == ball and b[i + 2][j + 2] == ball and b[i + 3][j + 3] == ball:
                return True;

    # Check diagonal wins (negative slope)
    for i in range(row_count - 3):
        for j in range(3, col_count):
            if b[i][j] == ball and b[i + 1][j - 1] == ball and b[i + 2][j - 2] == ball and b[i + 3][j - 3] == ball:
                return True

    return False

def win_position(b,ball): #score_position
    score=0
    for i in range(row_count):
        row_arr=[int(i) for i in list(b[i,:])]
        for j in range(col_count-3):
            window=row_arr[j:j+win_length]
            if window.count(ball)==4:
                score+=100
            elif window.count(ball)==3 and window.count(empty)==1:
                score+=10
    return score
def get_valid_locations(b):
    valid_locations=[]
    for i in range(col_count):
        if is_valid_column(b,i):
            valid_locations.append(i)
    return valid_locations

def best_score(b,ball): #pick_best_move
    valid_locatons=get_valid_locations(b)
    best_score=0
    best_col=random.choice(valid_locatons)
    for i in valid_locatons:
        row = check_row(b,i)
        temp_board=b.copy()
        ball_placement(temp_board,row,i,ball)
        score= win_position(temp_board,ball)
        if best_score>score:
            best_col=i

    return best_col
def darw_UI_board(b):
    for i in range(col_count):
        for j in range(row_count):
            pygame.draw.rect(screen,white,(i*box_size , j*box_size+box_size , box_size , box_size))
            pygame.draw.circle(screen, black,(int(i * box_size + box_size / 2), int(j * box_size + box_size + box_size / 2)), radius)
    for i in range(col_count):
        for j in range(row_count):
            if b[j][i] == human_ball:
                pygame.draw.circle(screen, red,(int(i * box_size + box_size / 2),height-int(j * box_size  + box_size / 2)),radius)
            elif b[j][i]==AI_ball:
                pygame.draw.circle(screen, yellow,(int(i * box_size + box_size / 2), height-int(j * box_size  + box_size / 2)),radius)

    pygame.display.update()

b=board()
flip_board(b)
game_over= False

pygame.init()
box_size = 80
width = col_count*box_size
height=(row_count+1)*box_size
size=(width,height)
radius=int(box_size/2 - 5)
screen=pygame.display.set_mode(size)
darw_UI_board(b)
pygame.display.update()
myfont = pygame.font.SysFont("monospace",60)
turn=random.randint(human,AI)
while not game_over:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen,black,(0,0,width,box_size))
            posx = event.pos[0]
            if turn == human:
                pygame.draw.circle(screen,red,(posx,int(box_size/2)),radius)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, black, (0, 0, width, box_size))
            if turn == human:
                posx = event.pos[0]
                column = int(math.floor(posx/box_size))

                if is_valid_column(b, column):
                    row = check_row(b, column)
                    ball_placement(b, row, column, human_ball)

                    if check_win(b, human_ball):
                       label = myfont.render("PLAYER 1 WINSS!!!",1,red)
                       screen.blit(label,(40,10))
                       game_over = True

                    turn += 1
                    turn = turn % 2
                    flip_board(b)
                    darw_UI_board(b)


    if turn == AI and not game_over:
        column=best_score(b,AI_ball)
        # column = random.randint(0, col_count - 1)

        if is_valid_column(b, column):
            pygame.time.wait(500)
            row = check_row(b, column)
            ball_placement(b, row, column, AI_ball)
            if check_win(b, AI_ball):
                label = myfont.render("PLAYER 2 WINSS!!!", 2, yellow)
                screen.blit(label, (40, 10))
                game_over = True

            flip_board(b)
            darw_UI_board(b)
            turn += 1
            turn = turn % 2

    if game_over:
        pygame.time.wait(3000)
