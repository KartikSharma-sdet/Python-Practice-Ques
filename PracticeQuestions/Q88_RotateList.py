import Input_Keywords.input as input

# Rotate Array
# Problem: Rotate the array to the right by k steps.

def rotateList():

    list = input.inputList()
    steps = input.inputInteger()
    list2 = []

    for i in range(steps+1, len(list)):
        list2.append(list[i])

    for i in range(0, steps+1):
        list2.append(list[i])

    print(list2)

rotateList()