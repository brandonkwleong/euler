#!/usr/bin/python

# find sum of all primes below 1000?
# how do i find a prime?

import math

def isNumPrime(number):
    numIsPrime = False
    
    if number <= 3:
        return True

    if number % 2 == 0:
        return False

    for x in range(2, int(math.sqrt(number))+1):
        if number % x == 0:
            return False

    return True

finalAnswer = 0
for x in range(2,2000000):
    if isNumPrime(x):
        print "{} is prime".format(x)
        finalAnswer += x

print finalAnswer
