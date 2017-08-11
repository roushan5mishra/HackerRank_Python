import sys

s_len = int(raw_input().strip())
s = raw_input().strip()
count = 0
def validate(x):
    for i in range(len(x)-1):
        if x[i] == x[i+1]:
            return False
    return True
        
temp = list(set(s))
for x in range(len(temp)):
    for y in range(x+1, len(temp)):
                   test = [i for i in s if i == temp[x] or i == temp[y]]
                   if validate(test):
                        count = max(len(test), count)
                   

print count    
