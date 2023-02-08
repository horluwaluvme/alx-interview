#!/usr/bin/python3
'''Generate the minimum operations
'''



def minOperations(n):


    """
    Compute the fewest number of operations needed to result 
    in exactly n H characters in the file.
    """
    
    normal = 0

    minumum = 2

    while n > 1:

        while n % minumum == 0:

            normal += minumum

            n /= minumum

        minumum += 1

    return normal
