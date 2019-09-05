#https://www.hackerrank.com/challenges/extra-long-factorials/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(num):
        n=num
        p=1
        for i in range(1,n+1):
                p=p*i
        print(p)


if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)

