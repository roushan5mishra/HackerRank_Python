#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

pd = []
sd = []
for i in range(len(a)):
    pd.append(a[i][i])
    sd.append(a[i][-i-1])


print abs(sum(pd)-sum(sd))
    
