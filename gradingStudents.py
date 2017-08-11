#!/bin/python

import sys

def solve(grades):
    
    # Complete this function
    temp = []
    
    for i in grades:
        if (i < 38):
            temp.append(i)
        else:
            if ((((i/5)+1)*5)-i) >= 3:
                temp.append(i)
            elif ((((i/5)+1)*5)-i) < 3:
                temp.append((((i/5)+1)*5))
    return temp
            

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))


