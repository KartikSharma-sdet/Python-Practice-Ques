import Input_Keywords.input as input

# 1512. Number of Good Pairs
# Given an array of integers nums, return the number of good pairs.
#
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

def numberOfGoodPairs():

    list = input.inputList()
    count = 0

    for i in range(len(list)):
        num1 = list[i]
        for j in range(i+1, len(list)):
            num2=list[j]
            if(num1 == num2 and i<j):
                print(f"({i}, {j})")
                count += 1

    print(f"The count is {count}")

numberOfGoodPairs()