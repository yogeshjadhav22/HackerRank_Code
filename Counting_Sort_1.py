#https://www.hackerrank.com/challenges/countingsort1/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
        #print(arr)
        dd=max(arr)
        dd=dd+1
        print(dd)
        ar=[0]*100
        #print(ar)
        for i in arr:
                for j in range(0,len(ar)):
                        if(i==j):
                                ar[j]=ar[j]+1
       
        return(ar)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

