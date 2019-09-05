#https://www.hackerrank.com/challenges/lonely-integer/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lonelyinteger function below.
def lonelyinteger(a):
    at=[]
    for i in a:
            if i not in at:
                    at.append(i)
    for i in at:
            count=0
            for j in a:
                if(i==j):
                    count+=1            
            if(count==1):
                return(i)
                break
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()

