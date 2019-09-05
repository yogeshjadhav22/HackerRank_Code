#https://www.hackerrank.com/challenges/find-the-median/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findMedian function below.
def findMedian(arr):
        #print(arr)
        p=sorted(arr)
        if(len(p)%2!=0):
                t=int(len(arr)/2)
                #print(t)
                return(p[t])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

