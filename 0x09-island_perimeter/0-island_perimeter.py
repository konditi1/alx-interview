#!/usr/bin/python3
"""Island Perimeter
"""


def island_perimeter(grid):
    """Calculates the perimeter of an island represented by a grid.

    Args:
    grid (list[list[int]]): A 2D grid representing the island where:
        - 0 represents water.
        - 1 represents land.

    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0

    # Check if grid is a valid 2D list of integers
    if not isinstance(grid, list):
        return 0

    # Iterate through each cell in the grid
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 0:
                continue

            # Check if the current cell has water neighbors
            top_edge = i == 0 or grid[i - 1][j] == 0
            bottom_edge = i == len(grid) - 1 or grid[i + 1][j] == 0
            left_edge = j == 0 or row[j - 1] == 0
            right_edge = j == len(row) - 1 or row[j + 1] == 0

            # Increment the perimeter based on water neighbors
            perimeter += top_edge + bottom_edge + left_edge + right_edge

    return perimeter
