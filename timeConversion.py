#!/bin/python

import sys

def timeConversion(s):
    # Complete this function
    temp1 = s[-2:]
    temp2 = int(s[:2])
    
    if temp1.upper() == 'PM':
        if temp2 < 12:
            temp2 +=12
        elif temp2 == 12:
            temp2 = 12
    elif temp1.upper() == 'AM':
        if temp2 < 12:
            temp2 = s[:2]
        elif temp2 == 12:
            temp2 = '00'
    return str(temp2)+s[2:-2]
    
        

s = raw_input().strip()
result = timeConversion(s)
print(result)
