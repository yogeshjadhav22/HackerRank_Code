#https://www.hackerrank.com/challenges/mini-max-sum/problem
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
     p=max(arr)
     q=min(arr)
     arr.remove(p)
     s1=sum(arr)
     arr.append(p)
     arr.remove(q)
     s2=sum(arr)
     print s1,s2
     
if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    miniMaxSum(arr)

