#!/usr/bin/python3

""" You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""

def canUnlockAll(boxes):
    """ Write a method that determines if all the boxes can be opened.
    @Prototype: def canUnlockAll(boxes)
    @boxes is a list of lists
    @key with the same number as a box opens that box
    @You can assume all keys will be positive integers
    @There can be keys that do not have boxes
    @first box boxes[0] is unlocked
    @Return True if all boxes can be opened, 
    @else return False@boxes is a list of    lists
    """

    keys = [0]

    for number in keys:

        for n in boxes[number]:

            if n not in keys and n < len(boxes):

                keys.append(n)

    return len(keys) == len(boxes)
