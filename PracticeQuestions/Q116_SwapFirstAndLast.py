import Input_Keywords.input as input

# Swap the first and last element

def swapFirstLast():

    list = input.inputList()

    if len(list) >= 2:
        list[0], list[-1] = list[-1], list[0]

    print(list)

swapFirstLast()