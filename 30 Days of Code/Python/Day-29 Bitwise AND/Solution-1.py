#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

# Brute-force solution — Time Complexity: O(N^2)
#
# Goal: Find the maximum value of (A & B) where:
#       1 ≤ A < B ≤ N and (A & B) < K
#
# Approach:
# - Iterate through all pairs (A, B) such that A < B ≤ N
# - For each pair, compute A & B
# - If the result is less than K and greater than current max_val, update max_val
#
# Note:
# - This approach is simple but inefficient for large N, as it checks every possible pair.
# - Suitable only when N is reasonably small (e.g., ≤ 10^3).

def bitwiseAnd(N, K):
    # Write your code here
    max_val = 0
    for A in range(1, N + 1):
        for B in range(A + 1, N + 1):
            val = A & B
            if val < K and val > max_val:
                max_val = val
    return max_val
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()
