__author__ = "Woohyun Cho (aka KafuChinoDesu in GitHub)"


# This file is for separating user i/o from main game for future GUI implementation.

def print_board(board, w, h):
    x_pos = 0
    y_pos = 0
    print(("+-" * w) + "+")
    for y_pos in range(0, w):
        line = ""
        for x_pos in range(0, h):
            line += "|{0}".format(board[x_pos][y_pos])
        print(line + "|")
        print(("+-" * w) + "+")


def get_input():
    input_ = input_("Input(ex: \"1,1\" for 1,1):")
    return input_
