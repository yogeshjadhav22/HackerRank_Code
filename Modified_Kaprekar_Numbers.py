#https://www.hackerrank.com/challenges/kaprekar-numbers/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    cnt=0
    for i in range(p,q+1):
        ar=[]
        p1=0
        f=i
        t=str(f)
        tt=len(t)
        p1=i*i
        p1=str(p1)
        if(len(p1)==2):
                s=int(p1[:1])+int(p1[1:2])
                if(i==s):
                    cnt+=1
                    print(i,end=" ")
        elif(len(p1)==1):
                if(int(p1)==i):
                    cnt+=1
                    print(i,end=" ")
        else:
            rr=len(p1)-tt

            q1=int(p1[:rr])+int(p1[-tt:])
            if(q1==i):
                cnt+=1
                print(i,end=" ")
    if(cnt==0):
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
    








if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)

