import Input_Keywords.input as input

def flatten2DList():

    print("Enter length of the 2D list")
    length2D = input.inputLength()
    list2D=[]
    newList = []
    count = 0

    while(count < length2D):
        print(f"Enter list {count+1}")
        listTemp = input.inputListWithString()
        list2D.append(listTemp)
        count += 1

    for list in list2D:
        for val in list:
            newList.append(val)

    print(newList)

flatten2DList()