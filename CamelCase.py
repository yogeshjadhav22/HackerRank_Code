#https://www.hackerrank.com/challenges/camelcase/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
            count=0
            for i in range(0,len(s)):
                p=s[i].upper()
                if(s[i]==p):
                    count+=1

            return(count+1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()

