"""
Author: Michael Urban (c) 2019
Email: echo ur3an221g5ail4com | tr 1345 @b.m

Q: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?  

Notes: Solved without data structures.

"""
import problem1_1 as prob

stringPass = 'asdf'
stringFail = 'aasdf'


def test_findDupePass():
    assert prob.findDupe(stringPass) == True
    print('String ' + stringPass + ' yields in True')


def test_findDupeFail():
    assert prob.findDupe(stringFail) == False
    print('String ' + stringFail + ' yields in False')