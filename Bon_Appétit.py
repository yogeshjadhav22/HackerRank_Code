#https://www.hackerrank.com/challenges/bon-appetit/problem
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
       p=bill[k]
       bill.remove(p)
       d=sum(bill)
       d1=d/2
       if d1==b:
            print"Bon Appetit"
       else:
           bb=b-d1
           print bb
   
      
 

if __name__ == '__main__':
    nk = raw_input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = map(int, raw_input().rstrip().split())

    b = int(raw_input().strip())

    bonAppetit(bill, k, b)

