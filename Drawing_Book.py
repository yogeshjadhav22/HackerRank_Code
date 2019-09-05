#https://www.hackerrank.com/challenges/drawing-book/problem
#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
        if(p==1):
            p=0
            return(p)
        elif(n%2==0 and n==p):
            return(0)
        elif(n==p):
            return(0)
        else:
            cnt=0
            for i in range(1,n,2):
                if(i<p):
                    cnt+=1
            print(cnt)
            pnt=0
            if(p%2==0):
                for i in range(n-1,1,-2):
                    if(i>p):
                        pnt+=1
                        print(pnt)
            else:
                for i in range(n,1,-2):
                    if(i>p):
                        pnt+=1
            print(pnt)
            cc=min(cnt,pnt)
            return(cc)

    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

