# import sys

# def insertion_sorting(given_list):
#     cur_min = sys.maxsize
#     min_ind = 0
#     for j in range(len(given_list)):
#         i = j
#         while i < len(given_list):
#             if cur_min > given_list[i]:
#                 cur_min = given_list[i]
#                 min_ind = i
#             i+=1
#         temp = given_list[j]
#         given_list[j] = given_list[min_ind]
#         given_list[min_ind] = temp
#         cur_min = sys.maxsize
#         min_ind = 0
#     return given_list

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    def printArr(g_list):
        to_print = ""
        for a in range(len(g_list)):
            if a != len(g_list)-1:
                to_print += str(g_list[a]) + " "
            else:
                to_print += str(g_list[a])
        return to_print
    
    j = len(arr)-1
    cur = arr[n-1]
    while j >=0:
        if cur < arr[j-1]:
            arr[j] = arr[j-1]
            print(printArr(arr))
        elif cur >= arr[j-1]:
            arr[j] = cur
            print(printArr(arr))
            break
        if j-1 ==0:
            arr[j-1] = cur
            print(printArr(arr))
            break
        j -=1
        
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)