#https://www.hackerrank.com/challenges/funny-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(str1):
        p=list(str1)
        li=[]
        for i in range(0,len(p)):
                t=ord(p[i])
                li.append(t)
        pi=(li[::-1])
        flag=0
        for i in range(0,len(pi)-1):
                p1=li[i]-li[i+1]
                q1=pi[i]-pi[i+1]
                r=abs(p1)-abs(q1)
                if(r!=0):
                        flag=1
                        break
        if(flag==1):
                return "Not Funny"
        else:
                return "Funny"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()

