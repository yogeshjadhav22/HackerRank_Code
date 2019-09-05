#https://www.hackerrank.com/challenges/flipping-bits/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(st):
        p=bin(st)
        t=len(p)
        n=32-t-1
        j=0
        q="0"
        k=2
        for i in range(0,32+2):
                if(i==0):
                        pass
                elif(i==1):
                        q+='b'
                elif(j<=n+2):
                        q+='1'
                        j+=1
                elif(i>=j-1):
                        if(p[k]=='0'):
                                q+='1'
                                k+=1
                        else:
                                q+='0'
                                k+=1

        dh=int(q,2)
        return(dh)

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

