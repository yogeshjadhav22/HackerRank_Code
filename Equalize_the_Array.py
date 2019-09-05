#https://www.hackerrank.com/challenges/equality-in-a-array/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
        at=[]
        p=0
        for i in arr:
                if i not in at:
                        at.append(i)
        for i in at:
                cnt=0
                for j in arr:
                        if(i==j):
                                cnt+=1
                if(cnt>=p):
                        p=cnt
        return(len(arr)-p)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

