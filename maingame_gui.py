import pygame

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
w, h = 10, 10
Board = [[0 for x in range(w)] for y in range(h)]

pygame.init()

size = width, height = 510, 510
black = 0, 0, 0
white = 255, 255, 255
rose_gold = 183, 110, 121
gold = 212, 175, 55

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 40
HEIGHT = 40

# This sets the margin between each cell
MARGIN = 10

screen = pygame.display.set_mode(size)
pygame.display.set_caption("")

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
            if winner is None:
                now = pygame.time.get_ticks()
                if now - last >= cooldown:
                    last = now
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    # Set that location to one
                    if Board[row][column] == 0:
                        Board[row][column] = turn
                    if turn == 1:
                        turn = 2
                    elif turn == 2:
                        turn = 1
                    print("Click ", pos, "Grid coordinates: ", row, column)
                    winner = gameroutine.checkstone(Board, w, h, 0)

    # Set the screen background
    screen.fill(black)

    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = white
            if Board[row][column] == 1:
                color = rose_gold
            elif Board[row][column] == 2:
                color = gold
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    if winner is not None:
        print("Winner : ", winner)
        screen.fill(black)
        font = pygame.font.Font(None, 30)
        text = font.render("Player {} won the game!".format(winner), 1, gold)
        textpos = text.get_rect()
        textpos.centerx = screen.get_rect().centerx
        textpos.centery = screen.get_rect().centery
        screen.blit(text, textpos)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
