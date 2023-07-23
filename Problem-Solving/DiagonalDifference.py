#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    left_diagonal = 0
    right_diagonal = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i == j:
                left_diagonal += arr[i][j]
            if i + j == n - 1 :
                right_diagonal += arr[i][j]
                
    if left_diagonal > right_diagonal:
        return left_diagonal-right_diagonal
    else:
        return right_diagonal-left_diagonal   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
