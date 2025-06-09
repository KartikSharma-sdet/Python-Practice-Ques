import Input_Keywords.input as input

# Replace Every Element with the Difference from Max Value


def replaceWithDifferenceFromMaxValue():

    list = input.inputList()
    Max = 0
    Max = max(list)

    for i in range(len(list)):
        temp = list[i]
        list[i] = Max-temp

    print(list)

replaceWithDifferenceFromMaxValue()