#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    #temp = 0
    #m = max(ar)
    #for i in range(n):
        #if ar[i] == m:
            #temp +=1
    #return temp
    return ar.count(max(ar))
        
        

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
