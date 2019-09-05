#https://www.hackerrank.com/challenges/apple-and-orange/problem


import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
      d1=[]
      d2=[]
      for i in range(0,len(apples)):
          w=a+apples[i] 
          d1.append(w)
      for i in range(0,len(oranges)):
          w=b+oranges[i] 
          d2.append(w)
      cn1=0
      cn2=0
      for i in d1:
          if s<=i and i<=t:
              cn1=cn1+1

      for i in d2:
          if s<=i and i<=t:
              cn2=cn2+1        
      print cn1
      print cn2        

if __name__ == '__main__':
    st = raw_input().split()

    s = int(st[0])

    t = int(st[1])

    ab = raw_input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = map(int, raw_input().rstrip().split())

    oranges = map(int, raw_input().rstrip().split())

    countApplesAndOranges(s, t, a, b, apples, oranges)

