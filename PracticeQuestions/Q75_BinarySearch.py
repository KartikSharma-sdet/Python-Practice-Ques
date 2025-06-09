import Input_Keywords.input as input

# 704. Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.

def binarySearch():

    list = input.inputList()
    list.sort() #given in question
    target = input.inputInteger()

    i = 0
    j = len(list)
    mid = len(list) // 2
    res = 0
    count = 0

    while(i<j):
        mid = (i + j)//2
        res = list[mid]

        if res > target:
            j = mid
        elif res < target:
            i = mid
        else:
            count += 1
            print(mid)
            break

    if count == 0 : print("Not Found")

binarySearch()
