__author__ = "Woohyun Cho (aka KafuChinoDesu in GitHub)"
# This file is for separating user i/o from main game for future GUI implementation.

def printboard(board, w, h):
    xpos = 0
    ypos = 0
    print(("+-"*w) + "+" )
    for ypos in range(0,w):
        line = ""
        for xpos in range(0,h):
            line += "|{0}".format(board[xpos][ypos])
        print(line + "|")
        print(("+-"*w) + "+" )

def getinput():
    input = input("Input(ex: \"1,1\" for 1,1):")
    return input
