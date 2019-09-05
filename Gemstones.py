#https://www.hackerrank.com/challenges/gem-stones/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gemstones function below.
def gemstones(arr):
    p=""
    for i in arr:
        p=p+i
    at=[]
    cnt=0
    for i in p:
        if i not in at:
            at.append(i)
    #print(at)
    t1=0
    for  q in at:
        for ii in arr:
            rr=q in ii
            if(rr==True):
                t1+=1
        
        if(len(arr)==t1):
            cnt+=1
        t1=0
    return(cnt)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

