#https://www.hackerrank.com/challenges/countingsort2/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
        #print(dd)
        ar=[0]*100
        #print(ar)
        pt=[]
        for i in arr:
                for j in range(0,len(ar)):
                        if(i==j):
                                ar[j]=ar[j]+1
        for i in range(0,len(ar)):
            if(ar[i]!=0):
                for j in range(0,ar[i]):
                    pt.append(i)
        return(pt)
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

