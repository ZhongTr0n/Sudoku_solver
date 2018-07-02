# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 09:02:43 2018

@author: bossaerts_bruno
"""


import numpy as np


#  puzzle = np.genfromtxt('C:\\PANDAS\\easy.txt' ,dtype='int')
puzzle = np.genfromtxt('/Users/bruno/Google Drive/Python/Sudoku Solver/easy.txt',dtype='int')



# Make list of tuples of all coordinates

x_coordinates = []
y_coordinates = []

# List of x-coordinates
for a in range(9):
    for b in range(9):
        (x_coordinates.append(a))
        
# List of y-coordinates
for a in range(9):
    for b in range(9):
        (y_coordinates.append(b))
        
# Merge lists
coordinates = (list(zip(x_coordinates, y_coordinates)))

# Remove all non-zero values from coordinates
# Now only the zero's (empty cells) remain
for i in list(zip(np.nonzero(puzzle)[0], np.nonzero(puzzle)[1])):
    coordinates.remove(i)

quarter_coordinates = []
for horizontal_block in range(3):
    block_startindex = (27*horizontal_block)
    for vert_block in range(3):
        vert_block_index = ((3*vert_block)+block_startindex)
        for final_index in range(3):
            for coordinate in range((vert_block_index+(9*final_index)),((vert_block_index+(9*final_index))+3)):
                quarter_coordinates.append(coordinate)
quarter_coordinates = np.array_split(quarter_coordinates, 9)



puzzle_list = np.concatenate(puzzle, axis=0)
cells_by_quarter = []
for i in quarter_coordinates:
    cells_by_quarter.append(puzzle_list[i])

    
    
# ----------------------------------------------------------

def check_rows(A):
    for i in A:
        if len(set([x for x in list(i) if x != 0])) != len([x for x in list(i) if x != 0]): 
            return False  # = er is een probleem met de rijen

def check_cols(A):
    A = np.transpose(A)
    for i in A:
        if len(set([x for x in list(i) if x != 0])) != len([x for x in list(i) if x != 0]):
            return False # = er is een probleem met de kolommen

def check_quarter(A):
    puzzle_list = np.concatenate(A, axis=0)
    cells_by_quarter = []
    for i in quarter_coordinates:
        cells_by_quarter.append(puzzle_list[i])
    for row in cells_by_quarter:
        if len(set([x for x in list(row) if x != 0])) != len([x for x in list(row) if x != 0]):
            return False  # = er is een probleem met de quarters


def fill_cell(index):
    possibilities = []
    puzzle[index] += 1
    # print(puzzle, end='\r', flush=True)
    for i in range(puzzle[index],10):
        puzzle[index] = i
        if (check_rows(puzzle) != False) and (check_cols(puzzle) != False) and (check_quarter(puzzle) != False):
            possibilities.append(i)
    if len(possibilities) == 0:
        puzzle[index] = 0
    else:
        puzzle[index] = min(possibilities)
            

index_counter = 0

while ((puzzle.size - np.count_nonzero(puzzle)) > 0):
    fill_cell(coordinates[index_counter])
    if puzzle[coordinates[index_counter]] == 0:
        index_counter -= 1
    else:
        index_counter += 1
        

print(puzzle)



    
    
    
    
