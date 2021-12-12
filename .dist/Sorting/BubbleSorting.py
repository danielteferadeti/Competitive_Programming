#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    num_swap = 0
    g_list = a
    for k in range(len(g_list)):
        for i in range(len(g_list)-1):
            if g_list[i] > g_list[i+1]:
                temp = g_list[i]
                g_list[i] = g_list[i+1]
                g_list[i+1] = temp
                num_swap+=1
    print("Array is sorted in " + str(num_swap) + " swaps.")
    print("First Element: " + str(g_list[0]))
    print("Last Element: " + str(g_list[len(g_list) - 1]))
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
