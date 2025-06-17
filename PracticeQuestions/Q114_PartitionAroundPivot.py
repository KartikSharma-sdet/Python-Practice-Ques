import Input_Keywords.input as input

def partitionAroundPivot():

    list = input.inputList()
    pivot = input.inputInteger()

    less = []
    equal = []
    greater = []

    for num in list:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        elif num > pivot:
            greater.append(num)

    print("RESULT :")
    print(f"less = {less}")
    print(f"equal = {equal}")
    print(f"greater = {greater}")

partitionAroundPivot()
