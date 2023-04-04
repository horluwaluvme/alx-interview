#!/usr/bin/python3
'''Generate prime numbers first
'''



def getPrimes(n):
    primes = []
    sieve = [True] * (n+1)
    for i in range(2, n+1):
        if sieve[i]:
            primes.append(i)
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return primes


'''Removes all multiples of a prime number from the list of nums
'''
def removeMultiples(prime, nums):
    for i in range(prime, nums[-1]+1, prime):
        if i in nums:
            nums.remove(i)

'''Calculates the winner in the game
'''
def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        primes = getPrimes(n)
        turn = 0 # 0 for Maria, 1 for Ben
        while primes:
            prime = primes.pop(0)
            if turn == 0:
                removeMultiples(prime, nums)
                turn = 1
            else:
                removeMultiples(prime, nums)
                turn = 0
        if turn == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins == ben_wins:
        return None
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return "Ben"
