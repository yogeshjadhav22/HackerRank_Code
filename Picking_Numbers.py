#https://www.hackerrank.com/challenges/picking-numbers/problem

    #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(aa):
        mm=0
        aa=sorted(aa)
        for i in range(0,len(aa)):
                cnt=0
                for j in range(i,len(aa)-1):
                        p=aa[i]-aa[j+1]
                        if(abs(p)<=1):
                                cnt+=1
                        else:
                                if(cnt>=mm):
                                        mm=cnt
                                
                                break
                        if(cnt>=mm):
                                mm=cnt
                                        
        return(mm+1)


    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

