import Input_Keywords.input as input

# LeetCode : 3194. Minimum Average of Smallest and Largest Elements
# You have an array of floating point numbers averages which is initially empty. You are given an array nums of n integers where n is even.
#
# You repeat the following procedure n / 2 times:
#
# Remove the smallest element, minElement, and the largest element maxElement, from nums.
# Add (minElement + maxElement) / 2 to averages.
# Return the minimum element in averages.

def minimum(list) -> int:
    min = list[0]

    for num in list:
        if num < min :
            min = num
    return min, list.index(min)


def maximum(list) -> int:
    max = list[0]

    for num in list:
        if num > max:
            max = num
    return max,  list.index(max)


def minAndMaxOfSmallestAndLargestElements():

    elements = input.inputList()
    averages = []       #given in question

    i = 0
    j = 0
    temp = 0
    count = 0

    while len(elements) > 0:
        min, i = minimum(elements)
        max, j = maximum(elements)
        if(i< len(elements)):
            elements.pop(i)
        if (j-1 >= 0 and (j-1) < len(elements)):
            elements.pop(j-1)
        temp = (min + max) / 2

        if count == 0:
            averages.append(temp)
            count += 1
        elif temp > averages[0]:
            averages.append(temp)
        else :
            averages.insert(0, temp)

    print(averages[0])

minAndMaxOfSmallestAndLargestElements()