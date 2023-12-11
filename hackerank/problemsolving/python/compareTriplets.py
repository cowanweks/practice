#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

os.environ['OUTPUT_PATH'] = "out.txt"


def compareTriplets(a, b):
    alice_points = 0
    bob_points = 0
    # Write your code here
    for a_rate, b_rate in zip(a, b):
        if a_rate > b_rate:
            alice_points += 1
        elif a_rate < b_rate:
            bob_points += 1
        if a_rate == b_rate:
            pass

    return f"{alice_points} {bob_points}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(result)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
