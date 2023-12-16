#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    space_prefix = n - 1

    for stair_count in range(1, n + 1):
        print("{}{}".format(" " * space_prefix, "#" * stair_count))
        space_prefix -= 1

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
