import numpy as np
row_count=6
col_count=7
def board():
    b=np.zeros((6,7))
    return b

def ball_placement(b,row,column,ball):
     b[row][column]=ball
def check_row(b,column):
    for i in range(row_count):
        if b[i][column]==0:
            return i
def is_valid_column(b,column):
    return b[5][column]==0

def flip_board(b):
    print(np.flip(b,0))

b=board()
flip_board(b)
turn=0
game_over= False

while not game_over:
    if turn==0:
        column=int(input("player 1: Make your selection between (0-6) : "))

        if is_valid_column(b,column):
            row = check_row(b,column)
            ball_placement(b,row,column,1)

    else:
        column=int(input("player 2: Make your selection between (0-6) : "))

        if is_valid_column(b, column):
            row = check_row(b, column)
            ball_placement(b, row, column, 2)

    flip_board(b)

    turn+=1
    turn = turn % 2
