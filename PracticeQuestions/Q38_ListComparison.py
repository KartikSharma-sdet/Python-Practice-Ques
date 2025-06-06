import Input_Keywords.input as input

def listComparision():

    length = input.inputLength()

    list1 = input.inputListWithoutLength(length)
    list2 = input.inputListWithoutLength(length)
    count = 0

    for num in list1:
        if(num in list2):
            count = 1
            print(num)

    if count == 0:
        print("No common element found")

listComparision()