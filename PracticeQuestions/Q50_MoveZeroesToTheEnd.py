import Input_Keywords.input as input

# Move zeroes to the end without using any additional data structure
# input = [1,2,0,4,0,8,0]
# output = [1,2,4,8,0,0,0]

def moveZeroes():

    list = input.inputList()

    i = 0
    j = 0

    while j < len(list):

        if list[j] != 0 :
            list[i] = list[j]
            if j != i:
                list[j] = 0
            i += 1
        j += 1

    print(f"The new list is {list}")

moveZeroes()

