#!/usr/bin/python3

"""
Contains a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):

    """
    Returns the fewest number of operations needed to result in exactly
    n H characters in the file.
    """

    normal = 0

    minimum = 2

    while n > 1:

        while n % minimum == 0:

            normal += minimum

            n /= minimum

        minimum += 1

    return normal
