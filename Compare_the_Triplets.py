##https://www.hackerrank.com/challenges/compare-the-triplets
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
        p=0
        q=0
        for i in range(0,len(a)):
                if a[i]>b[i]:
                    p=p+1
                elif a[i]<b[i]:
                    q=q+1
        return(p,q)        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = map(int, raw_input().rstrip().split())

    b = map(int, raw_input().rstrip().split())

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

