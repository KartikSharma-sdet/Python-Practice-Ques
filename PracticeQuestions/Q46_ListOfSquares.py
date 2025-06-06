import Input_Keywords.input as input

# input : [1,2,3,4,5]
# output : [1,4,9,16,25]

def listOfSquares():
    length = input.inputLength()
    list1 = input.inputListWithoutLength(length)

    list2 = []

    for num in list1:
        list2.append(num**2)

    print(list2)

listOfSquares()

