#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(arr):

    ar=[]
    cnt=0
    p=arr[0]
    ar.append(p)
    for i in range(1,len(arr)):
         if ar[i-1]>=arr[i]:
             ar.append(ar[i-1])
         else:
             ar.append(arr[i])
             cnt=cnt+1


    ar1=[]
    cnt1=0
    p=arr[0]
    ar1.append(p)
    for i in range(1,len(arr)):
        if ar1[i-1]<=arr[i]:
           ar1.append(ar1[i-1])
        else:
           ar1.append(arr[i])
           cnt1=cnt1+1

    return(cnt,cnt1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    scores = map(int, raw_input().rstrip().split())

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

