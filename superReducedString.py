import sys

def super_reduced_string(s):
    # Complete this function
    for i in range(len(s)):
        if (i < (len(s) -1)) and (s[i] == s[i+1]):
            s = s[:i]+s[i+2:]
            s = super_reduced_string(s)
    return s if s else 'Empty String'            

s = raw_input().strip()
result = super_reduced_string(s)
print(result)
