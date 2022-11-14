# Conway's game of life
# Implemented by me, based on Sweigert's code

from random import randint
from copy import deepcopy
from time import sleep

Width = 60
Height = 20

# The cells are a list of lists
NextCells = []
for x in range(Width):
    # First create a new column
    Column = []
    for y in range(Height):
        if randint(0,1) == 0:# Use this line to initiate the game with random cells
        #if (x, y) in ((1, 0), (2, 1), (0, 2), (1, 2), (2, 2)):# Start with this line to see a glider
            Column.append('#')# # represents a living cell
        else:
            Column.append(' ')# space represents a dead cell
    NextCells.append(Column)

# Main program loop
while True:
    print('\n\n\n\n\n')# Each step is a new line
    CurrentCells = deepcopy(NextCells)

    # Print current cells on the screen
    for y in range(Height):
        for x in range(Width):
            print(CurrentCells[x][y], end='')#Prints each space or #
        print()# Creates a blank line

    # Determine the next step (i.e. the hard part)
    for x in range(Width):
        for y in range(Height):
            # Get neighboring coordinates
            # Use modulo to make sure we are always in range
            LeftCoord = (x-1) % Width
            RightCoord = (x+1) % Width
            AboveCoord = (y-1) % Height
            BelowCoord = (y+1) % Height

            # Count number of living neighbors
            NumNeighbors = 0
            if CurrentCells[LeftCoord][AboveCoord] == '#':
                NumNeighbors += 1# Top left neighbor is alive
            if CurrentCells[x][AboveCoord] == '#':
                NumNeighbors += 1# Top neighbor is alive
            if CurrentCells[RightCoord][AboveCoord] == '#':
                NumNeighbors += 1# Top right neighbor is alive
            if CurrentCells[LeftCoord][y] == '#':
                NumNeighbors += 1# Left neighbor is alive
            if CurrentCells[RightCoord][y] == '#':
                NumNeighbors += 1# Right neighbor is alive
            if CurrentCells[LeftCoord][BelowCoord] == '#':
                NumNeighbors += 1# Bottom left neighbor is alive
            if CurrentCells[x][BelowCoord] == '#':
                NumNeighbors += 1# Bottom neighbor is alive
            if CurrentCells[RightCoord][BelowCoord] == '#':
                NumNeighbors += 1# Bottom right neighbor is alive

            # Change cells according to rules
            if CurrentCells[x][y] == '#' and (NumNeighbors == 2 or NumNeighbors == 3):
                NextCells[x][y] = '#'# This cell stays alive
            elif CurrentCells[x][y] == ' ' and NumNeighbors == 3:
                NextCells[x][y] = '#'# This cell comes to life
            else:
                NextCells[x][y] = ' '# This cell dies or stays dead
    sleep(1)# One second per step, to reduce flickering
    # End loop
