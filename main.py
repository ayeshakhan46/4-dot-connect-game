import numpy as np
row_count=6
col_count=7
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

            if check_win(b,1):
                print("PLAYER 1 WINSS ! ")
                game_over = True;
    else:
        column=int(input("player 2: Make your selection between (0-6) : "))

        if is_valid_column(b, column):
            row = check_row(b, column)
            ball_placement(b, row, column, 2)
            if check_win(b, 2):
                print("PLAYER 2 WINSS ! ")
                game_over = True;

    flip_board(b)

    turn+=1
    turn = turn % 2
