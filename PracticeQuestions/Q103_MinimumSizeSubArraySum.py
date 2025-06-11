import Input_Keywords.input as input

#Minimum Size Subarray Sum
#Find the smallest subarray with sum ≥ target.

def minimumSizeSubarraySum():

    list = input.inputList()
    target = input.inputInteger()

    minWindow = len(list) + 1
    currSum = 0

    low = 0
    high = 0

    while(high <len(list)):
        currSum += list[high]
        high += 1

        while currSum >= target:
            currWindow = high - low
            if currWindow < minWindow:
                minWindow = currWindow
            currSum -= list[low]
            low += 1

    if minWindow >= len(list):
        print("False")
    else :
        print(f"True, {minWindow}")

minimumSizeSubarraySum()

