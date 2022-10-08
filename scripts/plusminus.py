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
    positive, negative, zeroes = 0,0,0
    for i in arr:
        if i>0:
            positive+=1
        elif i<0:
            negative+=1
        else:
            zeroes+=1
    
    print("%.6f" %(positive/len(arr)))
    print("%.6f" %(negative/len(arr)))
    print("%.6f" %(zeroes/len(arr)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
