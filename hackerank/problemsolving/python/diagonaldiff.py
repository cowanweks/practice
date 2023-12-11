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
    # Initialize the difference
    difference = 0

    # Find the sum of the primary diagonal
    primary_diagonal_sum = 0
    for i in range(len(arr)):
        primary_diagonal_sum += arr[i][i]

    # Find the sum of the secondary diagonal
    secondary_diagonal_sum = 0
    for i in range(len(arr)):
        secondary_diagonal_sum += arr[i][len(arr) - 1 - i]

    # Calculate the absolute difference
    difference = abs(primary_diagonal_sum - secondary_diagonal_sum)

    return difference


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
