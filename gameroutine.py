# This Module checks if the stones are placed in 5 in the row.
__author__ = "Woohyun Cho (aka KafuChinoDesu in GitHub)"


def if_stones_are_in_5_in_the_row(board, w, h):
    for x in range(0, w - 5):
        for y in range(0, h - 5):
            if board[x][y] == board[x + 1][y] == board[x + 2][y] == board[x + 3][y] == board[x + 4][y]:
                if board[x][y] is not None and board[x][y] is not " ":
                    return board[x][y]
            elif board[x][y] == board[x][y + 1] == board[x][y + 2] == board[x][y + 3] == board[x][y + 4]:
                if board[x][y] is not None and board[x][y] is not " ":
                    return board[x][y]
            elif board[x][y] == board[x + 1][y + 1] == board[x + 2][y + 2] == board[x + 3][y + 3] == board[x + 4][y + 4]:
                if board[x][y] is not None and board[x][y] is not " ":
                    return board[x][y]
            elif board[x - 4][y] == board[x - 3][y + 1] == board[x - 2][y + 2] == board[x - 1][y + 3] == board[x][y + 4]:
                if board[x - 4][y] is not None and board[x - 4][y] is not " ":
                    return board[x - 4][y]
    return None
