#!/usr/bin/python3

""" You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""

def canUnlockAll(boxes):
    """ Write a method that determines if all the boxes can be opened.
    @Prototype: def canUnlockAll(boxes)
    """

    keys = [0]

    for number in keys:

        for n in boxes[number]:

            if n not in keys and n < len(boxes):

                keys.append(n)

    return len(keys) == len(boxes)
