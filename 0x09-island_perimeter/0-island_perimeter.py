#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.
    
    Args:
        grid (list of list of ints): A grid where 0 represents water and 1 represents land.
    
    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4
                
                # Check the left neighbor
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
                
                # Check the top neighbor
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
    
    return perimeter

