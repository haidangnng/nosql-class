#!/usr/bin/env python3
# coding: utf8

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises


# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
    # +++your code here+++

    res = []
    # 1st solution
    # for num in nums:
    #     if num not in res:
    #         res.append(num)

    # 2nd solution
    for index, num in enumerate(nums):
        if (not nums[index - 1] == num) or index == 0:
            res.append(num)

    return res


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def list_merge(list1, list2):
    # +++your code here+++
    size_1 = len(list1)
    size_2 = len(list2)

    res = []
    i, j = 0, 0

    while i < size_1 and j < size_2:
        if list1[i] < list2[j]:
            res.append(list1[i])
            i += 1

        else:
            res.append(list2[j])
            j += 1

    res = res + list1[i:] + list2[j:]
    return res


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
    # print("remove_adjacent")
    # test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    # test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    # test(remove_adjacent([]), [])

    print()
    print("list_merge")
    test(list_merge(["aa", "xx", "zz"], ["bb", "cc"]), ["aa", "bb", "cc", "xx", "zz"])
    test(list_merge(["aa", "xx"], ["bb", "cc", "zz"]), ["aa", "bb", "cc", "xx", "zz"])
    test(list_merge(["aa", "aa"], ["aa", "bb", "bb"]), ["aa", "aa", "aa", "bb", "bb"])


#############################################################################

if __name__ == "__main__":
    main()
