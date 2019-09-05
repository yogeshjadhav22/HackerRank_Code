#https://www.hackerrank.com/challenges/staircase
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    
    j=n-1
    for i in range(0,n):
        if i==n-1:
          print '#'*(n)

        else:
          print ' '*(j-1),'#'*(n-j)
          j=j-1


  
if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)
