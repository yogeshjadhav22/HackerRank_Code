#https://www.hackerrank.com/challenges/strong-password/problem
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, str1):
    p=0
    flag=0
    f1=0
    f2=0
    f3=0
    #print(n,str1)
    if(n<6):
        regex=re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if(regex.search(str1)== None):
            pass
        else:
            f1=1
        for i in str1:
            if(i.isdigit()==True):
                flag=1
            if(i.isupper()==True):
                f2=1
            if(i.islower()==True):
                f3=1
        if(f1==0):
                for i in str1:
                    if(i=='+' or i=='-'):
                        p=p-1
                        break

        #print(f1,flag,f2,f3)
        if(f1==0):
            p=p+1
        if(f2==0):
            p=p+1
        if(f3==0):
            p=p+1
        if(flag==0):
            p=p+1
        if(n+p<6):
            n=n+p
            t=6-n
            p=p+t
            return(p)
        else:
            return(p)
                        
        
    else:
        regex=re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if(regex.search(str1)== None):
            pass
        else:
            f1=1
        for i in str1:
            if(i.isdigit()==True):
                flag=1
            if(i.isupper()==True):
                f2=1
            if(i.islower()==True):
                f3=1
        #print(f1,flag,f2,f3)
        if(f1==0):
                for i in str1:
                    if(i=='+' or i=='-'):
                        p=p-1
                        break
        if(f1==0):
            p=p+1
        if(f2==0):
            p=p+1
        if(f3==0):
            p=p+1
        if(flag==0):
            p=p+1
        return(p)
        
        
    # Return the minimum number of characters to make the password strong

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    password = raw_input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()

