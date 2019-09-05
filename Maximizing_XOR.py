#https://www.hackerrank.com/challenges/maximizing-xor/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximizingXor function below.
def maximizingXor(l, r):
        mi1=00
        for i in range(l,r+1):
                for j in range(i,r+1):
                        #print(i^j)
                        tt=i^j
                        if(tt>=mi1):
                                mi1=tt
        return(mi1)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()

