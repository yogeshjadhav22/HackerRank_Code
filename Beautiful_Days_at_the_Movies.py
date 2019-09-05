#https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
        d=i
        arr=[]
        for i in range(i,j+1):
                arr.append(i)
        print(arr)
        for p in range(0,len(arr)):
                p1=str(arr[p])
                p4=p1[::-1]
                print("ch",p1)
                #p3=0
                #p1=arr[p]%10
                #p2=p1*10
                #p3=arr[p]/10
                #p4=p2+p3
                arr[p]=int(p4)
        #print(arr)
        count=0
        p=0
        for i in range(d,j+1):
                p1=i-arr[p]
                p=p+1
                if(p1%k==0):
                        count+=1

        return(count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()

