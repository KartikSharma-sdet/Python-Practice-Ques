import Input_Keywords.input as input

def xorOfAll():

    list = input.inputList()

    result = 0
    for i in range(len(list)):
        result = result ^ list[i]

    print(f"The XOR of all elements is {result}")

xorOfAll()