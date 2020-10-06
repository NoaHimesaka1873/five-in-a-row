import gameroutine
import gametermio

__author__ = "Woohyun Cho (aka KafuChinoDesu in GitHub)"
__year__ = "2018 - 2020"
__license__ = f"""
    Copyright (C) {__year__} {__author__}

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

gametermio.printb(Board, w, h)
while True:
    term_input = gametermio.inputb()
    input_x = int(term_input[0]) - 1
    input_y = int(term_input[2]) - 1
    Board[input_x][input_y] = "O"
    winner = gameroutine.checkstone(Board, w, h)
    gametermio.printb(Board, w, h)
    if winner is not None:
        print(winner + " won the game!")
        break
    term_input = gametermio.inputb()
    input_x = int(term_input[0]) - 1
    input_y = int(term_input[2]) - 1
    Board[input_x][input_y] = "X"
    winner = gameroutine.checkstone(Board, w, h)
    gametermio.printb(Board, w, h)
    if winner is not None:
        print(winner + " won the game!")
        break
