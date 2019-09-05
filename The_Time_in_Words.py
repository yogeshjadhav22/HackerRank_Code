#https://www.hackerrank.com/challenges/the-time-in-words/problem
#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the timeInWords function below.
def once(num):
    word = ''
    if num == '1':
        word = "one"
    if num == '2':
        word = "two"
    if num == '3':
        word = "three"
    if num == '4':
        word = "four"
    if num == '5':
        word = "five"
    if num == '6':
        word = "six"
    if num == '7':
        word = "seven"
    if num == '8':
        word = "eight"
    if num == '9':
        word = "nine"
    word = word.strip()
    return word

def ten(num):
    word = ''
    if num[0] == '1':
        if num[1] == '0':
            word = "ten"
        if num[1] == '1':
            word = "eleven"
        if num[1] == '2':
            word = "twelve"
        if num[1] == '3':
            word = "thirteen"
        if num[1] == '4':
            word = "fourteen"
        if num[1] == '5':
            word = "fifteen"
        if num[1] == '6':
            word = "sixteen"
        if num[1] == '7':
            word = "seventeen"
        if num[1] == '8':
            word = "eighteen"
        if num[1] == '9':
            word = "nineteen"
    else:
        text = once(num[1])
        if num[0] == '2':
            word = "twenty"
        if num[0] == '3':
            word = "thirty"
        if num[0] == '4':
            word = "fourty"
        if num[0] == '5':
            word = "fifty"
        word = word + " " + text
    word = word.strip()
    return word

def test1(h):
    test =h
    a = str(test)
    leng = len(a)
    if leng == 1:
           num = once(a)
    if leng == 2:
            num = ten(a)

    return(num)
def timeInWords(h, m):
    print(h,m)
    if(m<=30):
        if(m==0):
            num=test1(h)
            print (num)
            p=""
            p=num+" "+"o' clock"
            return(p)
        elif(m==30):
            num=test1(h)
            print (num)
            p=""
            p=("half past"+" "+num)
            return(p)
        elif(m==15):
            num=test1(h)
            p=""
            p=("quarter past"+" "+num)
            return(p)
        
        else:
            if(h==1 and m==1):
                num1=test1(m)
                num2=test1(h)
                p=""
                p=(num1+" "+"minute past"+" "+num2)
                return(p)
            else:
                num1=test1(m)
                num2=test1(h)
                p=""
                p=(num1+" "+"minutes past"+" "+num2)
                return(p)
    else:
        if(m==45):
            num=test1(h+1)
            p=""
            p=("quarter to"+" "+num)
            return(p)

        else:
            num=test1(h+1)
            m1=60-m
            num1=test1(m1)
            p=""
            p=(num1+" "+"minutes to"+" "+num)
            return(p)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()

