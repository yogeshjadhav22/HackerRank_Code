#https://www.hackerrank.com/challenges/plus-minus/problem
#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
        pp=[]
        lp=len(arr)
        
        q1=0
        q2=0
        q3=0
        for i in arr:
            if i>0:
               q1=q1+1
            elif i<0:
               q2=q2+1
            else:
               q3=q3+1
        p1=float(q1)/float(lp)
        p2=float(q2)/float(lp)
        p3=float(q3)/float(lp)
        pp.append(p1)
        pp.append(p2)
        pp.append(p3)
        for x in pp:
            print (x)
      
    # Write your code here.
    #

if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    plusMinus(arr)

