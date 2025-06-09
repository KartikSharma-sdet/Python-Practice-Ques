import Input_Keywords.input as input

# LeetCode : 1480. Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.

def runningSum():

    list = input.inputList()
    list2 = []
    result = 0

    for i in range(0,len(list)):
        result = 0
        for j in range(0,i+1):
            result += list[j]

        list2.append(result)

    print(list2)
runningSum()