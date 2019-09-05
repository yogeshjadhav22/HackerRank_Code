#https://www.hackerrank.com/challenges/encryption/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(str1):
    pp=str1.replace(" ","")
    ll=len(pp)
    p1=ll**0.5
    t1=math.floor(p1)
    t2=math.ceil(p1)
    st=[]
    i=0
    t=t2
    dd=t1*t2
    if(dd>=ll):
        while(i<ll):
            st.append(pp[i:t])
            i=i+t2
            t=t+t2
        n=len(st[0])
        qq=""
        for i in range(0,n):
            pp=""
            for j in st:
                if(i<len(j)):
                    pp=pp+j[i]
            qq=qq+pp
            qq=qq+" "
        return(qq)
    else:
        while(i<ll):
            st.append(pp[i:t])
            i=i+t2
            t=t+t2
        n=len(st[0])
        qq=""
        for i in range(0,n):
                        pp=""
                        for j in st:
                                if(i<len(j)):
                                        pp=pp+j[i]
                        qq=qq+pp
                        qq=qq+" "
        return(qq)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

