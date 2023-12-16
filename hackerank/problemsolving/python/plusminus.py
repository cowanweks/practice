#!/bin/python3

"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to (10^{-4}) are acceptable.

Example

arr = [1, 1, 0, -1, -1]

There are (n=5) elements, two positive, two negative and one zero.

Their ratios are (\frac{2}{5}=0.400000)
(\frac{2}{5}=0.400000) and
[\frac{1}{5}=0.200000]

Results are printed as:

                0.400000

                0.400000

                0.200000
Function Description

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

Parameters:

arr: An array of integers
Return value: None (void function)

Purpose:

This function calculates the ratios of positive, negative, and zero values in the provided array and prints them to the console.

Here's a breakdown of the code:

Line 1: Defines the function plusMinus with the parameter arr.
Line 3: Initializes two variables:
pos: Counts the number of positive numbers in the array.
neg: Counts the number of negative numbers in the array.
zero: Counts the number of zeros in the array.
Lines 5-7: Loops through each element in the array using a for loop.
Inside the loop, the code checks if the current element is positive, negative, or zero and increments the corresponding counter (pos, neg, or zero).
Lines 9-14: Calculates the ratios of positive, negative, and zero values by dividing each count by the total number of elements (n) and formatting the result to six decimal places.
Lines 16-18: Prints the calculated ratios to the console, each on a separate line.
"""

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    x, y, z = 0, 0, 0

    for index in range(0, len(arr)):
        if arr[index] > 0:
            x += 1

        elif arr[index] < 0:
            y += 1

        else:
            z += 1

    print("{:.6f}".format(x/len(arr)))
    print("{:.6f}".format(y/len(arr)))
    print("{:.6f}".format(z/len(arr)))




if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
