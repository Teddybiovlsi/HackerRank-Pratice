#!/bin/python3

import re

# Day 28: RegEx, Patterns, and Intro to Databases
# Task: Print an alphabetically-ordered list of first names for every user with a Gmail account.

if __name__ == '__main__':
    N = int(input().strip())  # Number of rows
    match_names = []

    for _ in range(N):
        firstName, emailID = input().strip().split()
        # Regex: check if email ends with '@gmail.com' and starts with lowercase letters
        if re.search(r'@gmail\.com', emailID):
            match_names.append(firstName)

    match_names.sort()

    for name in match_names:
        print(name)
