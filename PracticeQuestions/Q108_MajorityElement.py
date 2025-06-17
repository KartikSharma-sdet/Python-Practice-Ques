import Input_Keywords.input as input

def majorityElement():

    nums = input.inputList()
    target = 0
    count = 0

    for i in range(0, len(nums)):
        if count == 0:
            target = nums[i]
            count = 1
        elif nums[i] == target:
            count += 1
        else:
            count -= 1

    if count > len(nums)//2:
        print(f"The Majority Element is {target}")
    else :
        print("No majority element")

majorityElement()