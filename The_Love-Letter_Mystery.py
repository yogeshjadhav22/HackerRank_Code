#https://www.hackerrank.com/challenges/the-love-letter-mystery/problem
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(str1):
        cnt=0
        p=len(str1)-1
        for i in range(0,int(len(str1)/2)):
                t=ord(str1[i])
                q=ord(str1[p])
                if(t>q):
                        while(t!=q):
                                cnt+=1
                                t-=1
                        p-=1
                else:
                        while(t!=q):
                                cnt+=1
                                q-=1
                        p-=1
        return(cnt)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()

