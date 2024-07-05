#!/usr/bin/python3
"""Solves the lock boxes puzzle"""

def look_next_opened_box(opened_boxes):
    """Finds the next box that is opened but not yet checked.
    Args:
        opened_boxes (dict): Dictionary containing the status and keys of opened boxes.
    Returns:
        list: List of keys contained in the next box to check, or None if no such box exists.
    """
    for box in opened_boxes.values():
        if box['status'] == 'opened':
            box['status'] = 'checked'
            return box['keys']
    return None

def canUnlockAll(boxes):
    """Determines if all boxes can be opened.
    Args:
        boxes (list): List of boxes, each containing keys to other boxes.
    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    if len(boxes) == 0:
        return False
    if len(boxes) == 1 or boxes == [[]]:
        return True

    aux = {0: {'status': 'opened', 'keys': boxes[0]}}
    
    while True:
        keys = look_next_opened_box(aux)
        if keys:
            for key in keys:
                if key < len(boxes) and key not in aux:
                    aux[key] = {'status': 'opened', 'keys': boxes[key]}
        else:
            break

    return len(aux) == len(boxes)

def main():
    """Entry point"""
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False

if __name__ == '__main__':
    main()

