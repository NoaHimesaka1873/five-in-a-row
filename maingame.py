import gameroutine
import gametermio

__author__ = "Woohyun Cho (aka KafuChinoDesu in GitHub)"
__license__ = f"""
    Copyright (C) 2018 - 2019 {__author__}

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
w, h = 9, 9
Board = [[" " for x in range(w)] for y in range(h)]

print(__license__)
print("If you continue to use this software, you're agreeing to the license.")
print("Exit this program and DELETE IT IMMEDIATELY to deny.")
input("Press enter key to continue...")

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
