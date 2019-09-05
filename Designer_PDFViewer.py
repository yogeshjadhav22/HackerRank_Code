#https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    l=len(h)
    k=len(word)
    min1=00000
    for i in word:
        pp=ord(i)
        pp=pp-97
        if(h[pp]>=min1):
            min1=h[pp]
    q=k*min1
    return(q)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
SSSSS
