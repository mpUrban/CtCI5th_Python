"""
Author: Michael Urban (c) 2019
Email: echo ur3an221g5ail4com | tr 1345 @b.m

Q: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?  

Solved without data structures.

"""


def findDupe(str_):
    newArray = []
    dupeArray = []
    for char in str_:
        if char not in newArray:
            newArray.append(char)
        else:
            dupeArray.append(char)
    if (len(dupeArray) == 0):
        return True
    else:
        return False
    