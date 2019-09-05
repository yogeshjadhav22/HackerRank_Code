#https://www.hackerrank.com/challenges/cut-the-sticks/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    ar=[]
    while(sum(arr)!=0):
            min1=99999
            at=arr
            for i in range(0,len(arr)):
                if(arr[i]<=min1 and arr[i]>0):
                     min1=arr[i]

           # print(arr)
            cnt=0
            for i in range(0,len(arr)):
                if(arr[i]!=0):
                    cnt+=1
                    arr[i]=arr[i]-min1
            ar.append(cnt)
    return(ar)
    #print(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

