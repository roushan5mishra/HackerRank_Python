import sys

def simpleArraySum(n, ar):
    sum = 0
    for i in range(n):
        sum += ar[i]
    return sum
        
    # Complete this function

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = simpleArraySum(n, ar)
print(result)
