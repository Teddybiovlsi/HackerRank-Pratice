# HackerRank - String Validators
# Problem: https://www.hackerrank.com/challenges/string-validators/
#
# Objective:
# Given a string s, determine if it contains:
# 1. Any alphanumeric characters
# 2. Any alphabetical characters
# 3. Any digits
# 4. Any lowercase characters
# 5. Any uppercase characters
#
# For each check, print True if any such character exists, otherwise print False.

if __name__ == '__main__':
    s = input()  # Read the input string

    # Check if there is at least one alphanumeric character
    print(any(c.isalnum() for c in s))  

    # Check if there is at least one alphabetic character
    print(any(c.isalpha() for c in s))  

    # Check if there is at least one digit
    print(any(c.isdigit() for c in s))  

    # Check if there is at least one lowercase character
    print(any(c.islower() for c in s))  

    # Check if there is at least one uppercase character
    print(any(c.isupper() for c in s))  
