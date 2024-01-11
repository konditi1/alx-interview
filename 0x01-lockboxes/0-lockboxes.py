#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determine if all boxes in the given list can be unlocked.
    Parameters:
        boxes (list):
          A list of lists, where each inner list represents the keys in a box.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    # Set to keep track of the boxes that can be reached
    visited = set()

    # Start with the first box
    stack = [0]

    # Iterate through the stack
    while stack:
        current_box = stack.pop()

        # If the current box hasn't been visited, mark it as visited
        if current_box not in visited:
            visited.add(current_box)

            # Add keys from the current box to the stack
            stack.extend(boxes[current_box])

    # Check if all boxes have been visited
    return len(visited) == len(boxes)
