#https://www.hackerrank.com/challenges/sock-merchant/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

        arr1=[]
        for  i in ar:
            if i not in arr1:
                arr1.append(i)

        sum1=0
        for ii in arr1:
            count=0
            for i in range(0,len(ar)):
                if ii==ar[i]:
                   count+=1

                p=int(count/2)
                
            sum1=sum1+p
        return sum1



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

