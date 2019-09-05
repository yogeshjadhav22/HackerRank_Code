#https://www.hackerrank.com/challenges/strange-code/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    q=3
    p=3
    while(q<t):
        p=p*2
        q=q+p
    q=q-t
    return(q+1)        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()

