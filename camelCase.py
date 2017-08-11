import sys


s = raw_input().strip()


#a = 1
#b = 0
#c = 0
#d = []

#for i in range(len(s)):
 #   if s[i].isupper():
  #      a+=1
   #     c = i
    #    d.append(s[b:c])
     #   b = c
#d.append(s[b:])        
#print d
#print len(d)    

print (sum(map(str.isupper, s))+1)
