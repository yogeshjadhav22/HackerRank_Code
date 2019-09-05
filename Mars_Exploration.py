#https://www.hackerrank.com/challenges/mars-exploration/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(str1):
    #print(str1)
    p=len(str1)
    n=p/3
    count=0
    k=0
    t=3
    m="SOS"
    for i in range(0,int(n)):
        f=(str1[k:t])
        k=k+3
        t=t+3
        for j in range(0,len(f)):
            if(m[j]!=f[j]):
                count+=1    
            
    return(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()

