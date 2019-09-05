#https://www.hackerrank.com/challenges/permutation-equation/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(arr):
    # print(arr)
        at=[]
        n=len(arr)+1
        for i in range(1,n):
                cnt=1
                for j in arr:
                        if(i==j):
                                break
                        else:
                                cnt+=1
                p=1
                for j in arr:
                        if(cnt==j):
                                break
                        else:
                                p+=1
                at.append(p)
        return(at)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

