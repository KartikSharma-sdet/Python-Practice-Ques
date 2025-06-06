# Given an array arr[] of n integers and a target value,
# the task is to find whether there is a pair of elements
# in the array whose sum is equal to target.
#
# Input: arr[] = [0, -1, 2, -3, 1], target = -2
# Output: true
# Explanation: There is a pair (1, -3) with the sum equal to given target, 1 + (-3) = -2.

import Input_Keywords.input as input


def TwoSum():

    list = input.inputList()
    target = input.inputInteger()
    length = len(list)
    count = 0

    for i in range(length):
        temp = target-list[i]
        if temp in list:
            print(f"true as {list[i]} and {temp} both exist in the list and add in for {target}")
            count = 1
            break

    if count == 0:
        print("false")

TwoSum()