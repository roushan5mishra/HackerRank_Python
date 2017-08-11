#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

pos = 0
neg = 0
zer = 0

for i in arr:
    if i == 0:
        zer+=1
    elif i < 0:
        neg+=1
    elif i > 0:
        pos+=1
print float(pos)/(pos + neg +zer)
print float(neg)/(pos + neg +zer)
print float(zer)/(pos + neg +zer)
