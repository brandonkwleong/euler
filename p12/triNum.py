#!/usr/bin/python

import sys
import math

def numberOfDivisors(number):    
    numDiv = 0
    for x in range(1, int(math.sqrt(number))):
        if number % x == 0:
            numDiv += 1
            if x != number/x:
                numDiv += 1
    
    return numDiv

# sum of 1 -> number
def getTriangleNum(number): 
    return (number * (number+1))/2

x = 1
while x:
    triangleNumber = getTriangleNum(x)
    print "Triangle Num: {}".format(triangleNumber)

    divNum = numberOfDivisors(triangleNumber)
    print "# of divisors: {}".format(divNum)

    if (divNum >= 500):
        print "FINAL: {}".format(triangleNumber)
        break

    x += 1
    
print "DONE!"
