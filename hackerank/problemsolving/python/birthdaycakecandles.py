#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

os.environ['OUTPUT_PATH'] = "out.txt"

def birthdayCakeCandles(candles: list) -> int:
    # Write your code here

    largest_candle = candles[0]
    largest_candle_count = 0

    for index in range(0, len(candles)):
        if candles[index] >= largest_candle:
            largest_candle = candles[index]


    largest_candle_count = candles.count(largest_candle)
    print(largest_candle_count)
    return largest_candle_count

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
