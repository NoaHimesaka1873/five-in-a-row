import pygame
import argparse
import gameroutine

__author__ = "Woohyun Cho (aka KafuChinoDesu in GitHub)"
__year__ = "2018 - 2019"
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

parser = argparse.ArgumentParser(description="A Simple Five-in-a-row (Gomoku) game.")
parser.add_argument("-ww", help="Sets the width of the board.", type=int, default=15, metavar="width")
parser.add_argument("-hh", help="Sets the height of the board.", type=int, default=15, metavar="height")
args = parser.parse_args()
w, h = args.ww, args.hh  # Sets the width and height of the board
Board = [[0 for x in range(w)] for y in range(h)]  # Initializes the board

# This starts PyGame engine.
pygame.init()

# DO NOT EDIT THESE VALUES UNLESS IF YOU KNOW WHAT YOU'RE DOING
# You can edit these colours to whatever you want. Just be careful.
black = 0, 0, 0  # Colour Black
white = 255, 255, 255  # Colour White
rose_gold = 183, 110, 121  # Colour Rose Gold (Player 1 Colour)
gold = 212, 175, 55  # Colour Gold (Player 2 Colour)

# Sets player colours
p1colour = rose_gold
p2colour = gold

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 40
HEIGHT = 40

# This sets the margin between each cell
MARGIN = 10

size = width, height = (w * WIDTH) + ((w + 1) * MARGIN), (h * HEIGHT) + ((h + 1) * MARGIN)  # Sets the size of the window

screen = pygame.display.set_mode(size)  # Sets screen size according to size variable
pygame.display.set_caption("Five-in-a-row")  # Sets screen title

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

turn = 1
winner = None
cooldown = 300
last = pygame.time.get_ticks()
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # If no one won the game
            if winner is None:
                now = pygame.time.get_ticks()  # Gets the current game tick
                if now - last >= cooldown:
                    last = now  # Compares it with the cooldown to prevent misclick
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    # Set that location to one
                    if Board[row][column] == 0:
                        Board[row][column] = turn
                    # Swaps the turn
                    if turn == 1:
                        turn = 2
                    elif turn == 2:
                        turn = 1
                    # Log position and grid coordinates
                    print("Click ", pos, "Grid coordinates: ", row, column)
                    # Check if someone won the game
                    winner = gameroutine.checkstone(Board, w, h, 0)

    # Set the screen background
    screen.fill(black)

    # Draw the grid
    for row in range(h):
        for column in range(w):
            colour = white
            if Board[row][column] == 1:
                colour = p1colour
            elif Board[row][column] == 2:
                colour = p2colour
            pygame.draw.rect(screen,
                             colour,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # If there is a winner, fill the screen with solid black colour and say about who won the game
    if winner is not None:
        # Log the winner to the console
        print("Winner : ", winner)
        screen.fill(black)  # Fill the screen with black
        font = pygame.font.Font(None, 30)  # Set the font to whatever the system tells us to use
        text = font.render("Player {} won the game!".format(winner), 1, gold)  # Set the message
        # Set the position to the center of the screen
        textpos = text.get_rect()
        textpos.centerx = screen.get_rect().centerx
        textpos.centery = screen.get_rect().centery
        # Make the text visible
        screen.blit(text, textpos)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
