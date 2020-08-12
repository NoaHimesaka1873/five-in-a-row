# This Module checks if the stones are placed in 5 in the row.
__author__ = "Woohyun Cho (aka KafuChinoDesu in GitHub)"


def checkstone(board, w, h, checkagainst=" "):
    for x in range(0, w - 4):
        for y in range(0, h):
            if board[x][y] == board[x + 1][y] == board[x + 2][y] == board[x + 3][y] == board[x + 4][y]:
                if board[x][y] is not checkagainst:
                    return board[x][y]
    for x in range(0, w):
        for y in range(0, h - 4):
            if board[x][y] == board[x][y + 1] == board[x][y + 2] == board[x][y + 3] == board[x][y + 4]:
                if board[x][y] is not checkagainst:
                    return board[x][y]
    for x in range(0, w - 4):
        for y in range(0, h - 4):
            if board[x][y] == board[x + 1][y + 1] == board[x + 2][y + 2] == board[x + 3][y + 3] == board[x + 4][y + 4]:
                if board[x][y] is not checkagainst:
                    return board[x][y]
            if board[x][y + 4] == board[x + 1][y + 3] == board[x + 2][y + 2] == board[x + 3][y + 1] == board[x + 4][y]:
                if board[x][y + 4] is not checkagainst:
                    return board[x][y + 4]
    return None
