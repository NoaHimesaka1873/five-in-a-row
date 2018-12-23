import gameroutine
import gametermio
__author__ = "Woohyun Cho (aka KafuChinoDesu in GitHub)"

w, h = 10, 10;
Board = [[" " for x in range(w)] for y in range(h)]
ruwin = None

gametermio.printboard(Board, w, h)
while True:   
    input = gametermio.getinput()
    inputx, inputy = input.split()
    Board[inputx][inputy] = "O"
    ruwin = gameroutine.ifstonesarein5intherow(Board, w, h)
    if ruwin != None:
        print(ruwin + " won the game!")
        break
    gametermio.printboard(Board, w, h)
    input = gametermio.getinput()
    inputx, inputy = input.split()
    Board[inputx][inputy] = "X"
    ruwin = gameroutine.ifstonesarein5intherow(Board, w, h)
    gametermio.printboard(Board, w, h)
    if ruwin != None:
        print(ruwin + " won the game!")
        break
