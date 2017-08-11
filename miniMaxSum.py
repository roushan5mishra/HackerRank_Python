import sys

arr = map(int, raw_input().strip().split(' '))

#temp = []
#for i in range(len(arr)):
    #temp.append(sum(arr)-arr[i])
#result = []
#result.append(min(temp))
#result.append(max(temp))
#print result[0], result[1]

var = sum(arr)
print var-max(arr), var-min(arr)
