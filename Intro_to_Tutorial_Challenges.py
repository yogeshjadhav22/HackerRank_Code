#https://www.hackerrank.com/challenges/tutorial-intro/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the introTutorial function below.
def introTutorial(v, arr):
         for i in range(0,len(arr)):
                if(arr[i]==v):
                        return(i)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input())

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

