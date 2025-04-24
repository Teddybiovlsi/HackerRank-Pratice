# HackerRank - Basic Data Types - Lists
# Problem: https://www.hackerrank.com/challenges/python-lists
#
# Objective:
# Perform various operations on a list based on user input commands.
# Supported commands: insert, print, append, remove, sort, pop, reverse.

if __name__ == '__main__':
    N = int(input())  # Read number of commands
    
    list = []  # Initialize an empty list
    
    for _ in range(N):
        operate = input().split()  # Split input into command and arguments
        
        operate_str = operate[0].lower()  # Normalize command to lowercase

        # Execute the appropriate command
        if operate_str == 'insert':
            list.insert(int(operate[1]), int(operate[2]))  # insert(i, e)
        elif operate_str == 'print':
            print(list)  # print the list
        elif operate_str == 'append':
            list.append(int(operate[1]))  # append(e)
        elif operate_str == 'remove':
            list.remove(int(operate[1]))  # remove(e)
        elif operate_str == 'sort':
            list.sort()  # sort the list
        elif operate_str == 'pop':
            list.pop()  # pop last element
        elif operate_str == 'reverse':
            list.reverse()  # reverse the list
