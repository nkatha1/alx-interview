#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented by 1s in a grid of 0s and 1s.

    Args:
        grid (list of list of int): The 2D grid representation of the map.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Start with 4 edges for a land cell
                perimeter += 4

                # Subtract edges for neighboring land cells
                if row > 0 and grid[row - 1][col] == 1:  # Check cell above
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:  # Check cell to the left
                    perimeter -= 2

    return perimeter

