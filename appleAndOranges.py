#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

####### 1st method which I tried

#acount = 0
#ocount = 0
#for apples in apple:
 #   if s <= (apples+a)  and t >= (apples+a):
  #      acount += 1
#for oranges in orange:
#    if s <= (oranges+b)  and t >= (oranges+b):
 #       ocount += 1   
#print acount
#print ocount


####### This is 2nd efficient method

print sum([1 for i in apple if (i+a) >= s and (i+a) <= t])
print sum([1 for i in orange if (i+b) >= s and (i+b) <= t])
