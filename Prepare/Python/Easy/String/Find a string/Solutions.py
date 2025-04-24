# HackerRank - Basic Data Types - Strings
# Problem: https://www.hackerrank.com/challenges/find-a-string/
#
# Objective:
# Given two strings, count the number of times the second string (substring)
# occurs in the first string. Substring occurrences may overlap.
#
# Function Description:
# Complete the count_substring function below.
#
# Parameters:
# string string: the main string in which to search
# string sub_string: the substring to count
#
# Returns:
# int: the number of occurrences of sub_string in string (including overlaps)

def count_substring(string, sub_string):
    count = 0
    # Loop through the string with a sliding window the size of the substring
    for i in range(len(string) - len(sub_string) + 1):
        # Compare the current window with the target substring
        if string[i:i+len(sub_string)] == sub_string:
            count += 1  # Increment the counter if there's a match
    return count

if __name__ == '__main__':
    string = input().strip()       # Read the main string from input
    sub_string = input().strip()   # Read the substring to be searched
    print(count_substring(string, sub_string))  # Output the count
