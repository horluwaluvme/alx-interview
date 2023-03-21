#!/usr/bin/python3
"""
defining the function
"""

def makeChange(coins, total):
    # initialize a table to store the minimum number of coins needed for each sub-total
    table = [float('inf')] * (total + 1)
    table[0] = 0
    
    # iterate over each coin
    for coin in coins:
        # for each coin, iterate over each sub-total
        for i in range(coin, total+1):
            # calculate the minimum number of coins needed for the current sub-total
            table[i] = min(table[i], table[i-coin]+1)
    
    # if the final sub-total is still infinity, it means the total cannot be met
    if table[total] == float('inf'):
        return -1
    
    # otherwise, return the minimum number of coins needed to meet the total
    return table[total]

