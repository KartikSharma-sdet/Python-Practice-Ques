import Input_Keywords.input as input

# Longest Consecutive Increasing Sublist
# Track the current increasing sequence.

def longestConsecutiveIncreasingSublist():

    list = input.inputList()

    max = 1
    count = 1

    for i in range(1, len(list)):

        if list[i] > list[i-1]:
            count += 1
            if count > max:
                max = count

        else :
            count = 1
    print(max)

longestConsecutiveIncreasingSublist()