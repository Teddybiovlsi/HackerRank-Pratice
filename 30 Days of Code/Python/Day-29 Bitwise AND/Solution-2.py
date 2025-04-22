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

# Optimized Solution - Time Complexity: O(1)
#
# Goal: Find the maximum value of (A & B) where:
#       1 ≤ A < B ≤ N and (A & B) < K
#
# Insight:
# - The best candidate for (A & B) < K is (K - 1),
#   because it's the largest possible number below K.
#
# - If there exists a pair (A, B) such that A & B == (K - 1),
#   and both A and B are ≤ N, then (K - 1) is the answer.
#
# - To check this efficiently, we use: (K - 1) | K
#   If (K - 1) | K ≤ N, then such a pair exists.
#   Otherwise, we step down and return (K - 2).

def bitwiseAnd(N, K):
    # Write your code here
    return K-1 if ((K-1) | K) <= N else K-2
    

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
