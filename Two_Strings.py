#https://www.hackerrank.com/challenges/two-strings/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    dp=[]
    for i in s2:
        if i not in dp:
            dp.append(i)
    flag=0
    for i in dp:
        for j in s1:
            if(i==j):
                flag=1
                break
    if(flag==1):
        return("YES")
    else:
        return("NO")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

