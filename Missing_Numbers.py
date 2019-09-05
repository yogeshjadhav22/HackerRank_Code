#https://www.hackerrank.com/challenges/missing-numbers/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
        st=[]
        for i  in brr:
                if i not in st:
                        st.append(i)
        d1=sorted(arr)
        d2=sorted(brr)
        s1=sorted(st)
        mg=[]
        for i in s1:
                cnt1=0
                cnt2=0
                for j in range(0,len(d2)):
                        if(j>=len(d1)):
                                if(i==d2[j]):
                                        cnt2+=1
                        else:
                                if(i==d1[j]):
                                        cnt1+=1
                                if(i==d2[j]):
                                        cnt2+=1
                if(cnt1<cnt2):
                        mg.append(i)
        return(mg)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

