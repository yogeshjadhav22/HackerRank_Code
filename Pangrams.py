#https://www.hackerrank.com/challenges/pangrams/problem
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
        p=list(s)
        q=0
        str2=[]
        for i in range(0,len(p)):
                if p[i] not in str2:
                        str2.append(p[i])
        for i in range(0,len(str2)):
                if(str2[i]==' '):
                        q=i
                        break

        del str2[q]
        a=97
        b=65
        ptr=[]
        for i in range(0,26):
                flag=0
                q=chr(a)
                r=chr(b)
                for j in range(0,len(str2)):
                        if(str2[j]==q or str2[j]==r):
                                flag=1
                                break
                if(flag==1):
                        ptr.append(0)
                else:
                        ptr.append(1)
                a=a+1
                b=b+1
        flag1=0
        for i in range(0,len(ptr)):
                if(ptr[i]!=0):
                        flag1=1
                        break
        if(flag1==1):
                return "not pangram"
        else:
                return "pangram"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

