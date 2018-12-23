import gameroutine
__author__ = "Woohyun Cho (aka KafuChinoDesu in GitHub)"

w, h = 10, 10;
Board = [[" " for x in range(w)] for y in range(h)]
ruwin = None

gameroutine.printboard(Board, w, h)
while True:   
    input = input("Input(ex: \"1,1\" for 1,1):")
    inputx, inputy = input.split()
    Board[inputx][inputy] = "O"
    ruwin = gameroutine.ifstonesarein5intherow(Board, w, h)
    if ruwin != None:
        print(ruwin + " won the game!")
        break
    gameroutine.printboard(Board, w, h)
    input = input("Input(ex: \"1,1\" for 1,1):")
    inputx, inputy = input.split()
    Board[inputx][inputy] = "X"
    ruwin = gameroutine.ifstonesarein5intherow(Board, w, h)
    gameroutine.printboard(Board, w, h)
    if ruwin != None:
        print(ruwin + " won the game!")
        break
