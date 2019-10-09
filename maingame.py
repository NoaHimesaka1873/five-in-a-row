import gameroutine
import gametermio

__author__ = "Woohyun Cho (aka KafuChinoDesu in GitHub)"

w, h = 10, 10
Board = [[" " for x in range(w)] for y in range(h)]
gametermio.print_board(Board, w, h)
while True:
    term_input = gametermio.get_input()
    input_x = int(term_input[0])-1
    input_y = int(term_input[2])-1
    Board[input_x][input_y] = "O"
    winner = gameroutine.if_stones_are_in_5_in_the_row(Board, w, h)
    gametermio.print_board(Board, w, h)
    if winner is not None:
        print(winner + " won the game!")
        break
    term_input = gametermio.get_input()
    input_x = int(term_input[0])-1
    input_y = int(term_input[2])-1
    Board[input_x][input_y] = "X"
    gametermio.print_board(Board, w, h)
    winner = gameroutine.if_stones_are_in_5_in_the_row(Board, w, h)
    if winner is not None:
        print(winner + " won the game!")
        break
