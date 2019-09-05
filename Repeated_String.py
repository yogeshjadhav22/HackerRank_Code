#https://www.hackerrank.com/challenges/repeated-string/problem
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    ss=len(s)
    p1=n/ss
    p2=n%ss
    p=s.count('a')
    q=p1*p
    w=s[:p2]
    w1=w.count('a')
    r=q+w1
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

