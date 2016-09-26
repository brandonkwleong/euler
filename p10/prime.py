#!/usr/bin/python

# find sum of all primes below 1000?
# how do i find a prime?

import math

def isNumPrime(number):
    numIsPrime = False

    if number <= 3:
        return True

    for x in range(5, number, 2):
        if number % x == 0:
            return False

    return True

print "Summing primes..."

finalAnswer = 0
for x in range(1,2000000):
    if isNumPrime(x):
        finalAnswer += x

print finalAnswer

