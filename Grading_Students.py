#https://www.hackerrank.com/challenges/grading/problem
#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    dk=[]
    
#print ar
    for i in grades:
        if i<38:
           dk.append(i)
        else:
            p=i/5
            q=(p+1)*5
            p1=q-i
        
            if p1<3:
            
                dk.append(q)
            else:
                dk.append(i)
    return dk

    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    grades = []

    for _ in xrange(n):
        grades_item = int(raw_input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()

