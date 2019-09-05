#https://www.hackerrank.com/challenges/the-birthday-bar/problem
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    p1=0
    w=len(s)
    if len(s)==1:
        cnt=0
        for i in range(0,len(s)):
             p=0
             for j in range(0,m):
                p=p+s[i+j]

             if p==d:
                 cnt=cnt+1
 
        return cnt 
    else:    
        cnt=0
        for i in range(0,len(s)-1):
             p=0
             w1=w-i 
             q=p1
             if w1>m-1:
                 for j in range(0,m):
                   p=p+s[q]
                   q=q+1
                 if p==d:
                    cnt=cnt+1
                 p1=p1+1
             else:
                 break
        return cnt 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    s = map(int, raw_input().rstrip().split())

    dm = raw_input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

