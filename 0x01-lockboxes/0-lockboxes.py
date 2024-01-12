#!/usr/bin/python3
"""BOXES BOXES"""


def canUnlockAll(boxes):
    """
    Determines whether the boxes can be locked or not.
    """
    all_boxes = len(boxes)
    keyset = [0]
    counter = 0
    index = 0

    while index < len(keyset):
        setkey = keyset[index]
        for key in boxes[setkey]:
            if 0 < key < all_boxes and key not in keyset:
                keyset.append(key)
                counter += 1
        index += 1

    return counter == all_boxes - 1