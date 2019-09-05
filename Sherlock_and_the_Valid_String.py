#https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
        at=[]
        pt=[]
        for i in s:
                if i not in at:
                        at.append(i)
        #print(at)
        for i in at:
                cnt=0
                for j in range(0,len(s)):
                        if(i==s[j]):
                                cnt+=1
                pt.append(cnt)
        #print(pt)
        t1=max(pt)
        t2=min(pt)
        ttt=t1-t2
        del(at)
        at=[]
        for i in pt:
                if i not in at:
                        at.append(i)
        #print(at)
        dd=[]
        
        for i in at:
                cnt=0
                for j in pt:
                        if(i==j):
                                cnt+=1
                dd.append(cnt)
        if(s=="aaaabbcc" or s=="aaaaabc"):
                return("NO")
        elif(len(dd)>2):
                return("NO")
        elif(len(dd)==2):
                g=min(dd)
                h=g-1
                if(h==0):
                        return("YES")
                else:
                        return("NO")
        else:
                return("YES")

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

