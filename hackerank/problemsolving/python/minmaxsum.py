#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr: list):
    # Write your code here
    min_sum = 0
    max_sum = 0

    arr.sort()

    for index in range(0, 4):
        min_sum += arr[index]

    for index in range(1, 5):
        max_sum += arr[index]

    print("{} {}".format(min_sum, max_sum))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
