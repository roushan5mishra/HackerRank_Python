#!/bin/python

import sys

def aVeryBigSum(n, ar):
    mySum = 0
    for i in range(n):
        mySum += ar[i]
    return mySum
        

n = int(raw_input().strip())
ar = map(long, raw_input().strip().split(' '))
result = aVeryBigSum(n, ar)
print(result)
