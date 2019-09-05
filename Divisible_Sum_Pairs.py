#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count=0
    for i in range(0,len(ar)):
        pp=i+1
        while(pp<n):
          dd=ar[i]+ar[pp]
          pp+=1
          if(dd%k==0):
                count=count+1

    return(count)





 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

