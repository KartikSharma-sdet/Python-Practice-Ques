import Input_Keywords.input as input

# Reverse list without using any other data structure

def reverseList():

    list = input.inputList()

    for i in range(0, len(list)//2):

        temp = list[i]
        list[i] = list[len(list)-i-1]
        list[len(list) - i - 1] = temp

    print(list)

reverseList()