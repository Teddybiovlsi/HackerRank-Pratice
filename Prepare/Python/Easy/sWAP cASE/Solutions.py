# HackerRank - Basic Data Types - Lists
# Problem: https://www.hackerrank.com/challenges/swap-case
#
# Objective:
# You are given a string and your task is to swap cases.
# In other words, convert all lowercase letters to uppercase letters and vice versa.


def swap_case(s):
    string = ""
    for char in s:
        if char.isupper():
            string += char.lower()
        else:
            string += char.upper()
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
