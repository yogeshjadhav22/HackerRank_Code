#https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    cnt=0
    cnt1=0
    if x>z:
        for i in range(x,z,-1):
            cnt=cnt+1
    else:
        for i in range(x,z):
            cnt=cnt+1
     
    if y>z:
        for i in range(y,z,-1):
            cnt1=cnt1+1
    else:
        for i in range(y,z):
            cnt1=cnt1+1
                  
    if(cnt<cnt1):
          return("Cat A")
    elif(cnt>cnt1):
          return("Cat B")
    else:
          return("Mouse C")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        xyz = raw_input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()

