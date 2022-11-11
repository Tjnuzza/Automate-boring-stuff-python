# Conway's game of life
# Implemented by me, based on Sweigert's code

import random, time, copy

Width = 60
Height = 20

# The cells are a list of lists
NextCells = []
For x in range(Width):
    # First create a new column
    Column = []
    if random.randint(0,1) == 0:
        column.append('#')# # represents a living cell
    else:
        column.append(' ')# space represents a dead cell
    NextCells.append(Column)
