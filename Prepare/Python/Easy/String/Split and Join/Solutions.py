# HackerRank - Basic Data Types - Strings
# Problem: https://www.hackerrank.com/challenges/python-string-split-and-join
#
# Objective:
# Given a string of space-separated words, split the string on spaces
# and then join the words using a hyphen (-) as a delimiter.
#
# Function Description:
# Complete the split_and_join function below.
#
# Parameters:
# string line: a string of space-separated words
#
# Returns:
# string: the resulting string with words joined by hyphens

def split_and_join(line):
    split_line = line.split()       # Split the input string into a list of words
    joined_line = "-".join(split_line)  # Join the words using a hyphen
    return joined_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
