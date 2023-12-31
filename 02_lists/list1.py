#!/usr/bin/env python3

# coding: utf8

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.


# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
    res = 0
    for word in words:
        if len(word) < 2:
            continue
        if word[0] == word[-1]:
            res += 1
    return res


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
    # +++your code here+++
    sorted_list = sorted(words)
    index_x = 0
    for index, word in enumerate(sorted_list):
        if word.startswith("x"):
            sorted_list.insert(index_x, sorted_list.pop(index))
            index_x += 1

    return sorted_list


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = " OK "
    else:
        prefix = "  X "
    print("{p} got: {g}; expected: {e}".format(p=prefix, g=got, e=expected))


# Calls the above functions with interesting inputs.
def main():
    print("match_ends")
    test(match_ends(["aba", "xyz", "aa", "x", "bbb"]), 3)
    test(match_ends(["", "x", "xy", "xyx", "xx"]), 2)
    test(match_ends(["aaa", "be", "abc", "hello"]), 1)

    print()
    print("front_x")
    test(
        front_x(["bbb", "ccc", "axx", "xzz", "xaa"]),
        ["xaa", "xzz", "axx", "bbb", "ccc"],
    )
    test(
        front_x(["ccc", "bbb", "aaa", "xcc", "xaa"]),
        ["xaa", "xcc", "aaa", "bbb", "ccc"],
    )
    test(
        front_x(["mix", "xyz", "apple", "xanadu", "aardvark"]),
        ["xanadu", "xyz", "aardvark", "apple", "mix"],
    )


#############################################################################

if __name__ == "__main__":
    main()
