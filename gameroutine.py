#This Module checks if the stones are placed in 5 in the row.
__author__ = "Woohyun Cho (aka KafuChinoDesu in GitHub)"

def ifstonesarein5intherow(board, w, h):
    tempvar = None
    for x in range(0,w-4):
        for y in range(0,h-4):
            if board[x][y] == board[x+1][y] and board[x+1][y] == board[x+2][y] and board[x+2][y] == board[x+3][y] and board[x+3][y] == board[x+4][y]: 
                tempvar = board[x][y]
            elif board[x][y] == board[x][y+1] and board[x][y+1] == board[x][y+2] and board[x][y+2] == board[x][y+3] and board[x][y+3] == board[x][y+4]: 
                tempvar = board[x][y]
            elif board[x][y] == board[x+1][y+1] and board[x+1][y+1] == board[x+2][y+2] and board[x+2][y+2] == board[x+3][y+3] and board[x+3][y+3] == board[x+4][y+4]:
                tempvar = board[x][y]
            elif board[x-4][y] == board[x-3][y+1] and board[x-3][y+1] == board[x-2][y+2] and board[x-2][y+2] == board[x-1][y+3] and board[x-1][y+3] == board[x][y+4]:
                tempvar = board[x][y]
            else:
                tempvar = 0
