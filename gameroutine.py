#This Module checks if the stones are placed in 5 in the row.
__author__ = "Woohyun Cho (aka KafuChinoDesu in GitHub)"

function printboard(board, w, h)
    print(("+-"*w) + "+" )
    for y in w:
        line = ""
        for x in h:
            line += "|{0}".format(board[x][y])
        print(line + "|")
        print(("+-"*w) + "+" )
    print(("+-"*w) + "+" )




function ifstonesarein5intherow(board, w, h):
    for x in w-4:
        for y in h-4:
            if board[x][y] == board[x+1][y] and board[x+1][y] == board[x+2][y] and board[x+2][y] == board[x+3][y] and board[x+3][y] == board[x+4][y]: // check board horizontally
                return board[x][y]
            elif board[x][y] == board[x][y+1] and board[x][y+1] == board[x][y+2] and board[x][y+2] == board[x][y+3] and board[x][y+3] == board[x][y+4]: // check board up to down
                return board[x][y]
            elif board[x][y] == board[x+1][y+1] and board[x+1][y+1] == board[x+2][y+2] and board[x+2][y+2] == board[x+3][y+3] and board[x+3][y+3] == board[x+4][y+4]:
                return board[x][y]
            elif board[x-4][y] == board[x-3][y+1] and board[x-3][y+1] == board[x-2][y+2] and board[x-2][y+2] == board[x-1][y+3] and board[x-1][y+3] == board[x][y+4]:
                return board[x][y]
            else:
                return 0;