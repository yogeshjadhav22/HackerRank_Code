#https://www.hackerrank.com/challenges/time-conversion/problem
#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
        #print(s)
        l=len(s)
        p=s[l-2:]
        #print(p)
        if(p=="PM"):
                t=12
                q=int(s[:2])
                t=t+q
                if(t==24):
                    t=12
                #print("check",q,t)
                d=str(t)+s[2:l-2]
                return(d)

        else:   
                if(s[:2]=="12"):
                    t="00"
                    d=t+s[2:l-2]
                    return(d)
                else:
                    return(s[0:l-2])

                #print("check again")


    #
    # Write your code here.
    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

