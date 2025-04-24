# HackerRank - Basic Data Types - Strings
# Problem: https://www.hackerrank.com/challenges/python-mutations/
#
# Objective:
# Read a given string, change the character at a given index and then print the modified string.
#
# Function Description:
# Complete the mutate_string function in the editor below.
#
# Parameters:
# string string: the string to change
# int position: the index to insert the character at
# string character: the character to insert
#
# Returns:
# string: the altered string

def split_and_join(line):
    split_line = line.split()       # Split the input string into a list of words
    joined_line = "-".join(split_line)  # Join the words using a hyphen
    return joined_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
