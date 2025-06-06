import Input_Keywords.input as input

# input : [12,2432,543,46,75,888,4,7]

# output : 888  (Second Largest)

def findSecondLargestNumberInAList():

    list = input.inputList()

    firstMax = 0
    secondMax = 0

    for num in list :
        if num > firstMax:
            secondMax = firstMax
            firstMax = num

    print(f"Second Maximum number in {list} is {secondMax}")

findSecondLargestNumberInAList()












