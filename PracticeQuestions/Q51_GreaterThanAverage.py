import Input_Keywords.input as input

# input : [4,5,5,6]
# output : [6]

def greaterThanAverage():
    list = input.inputList()
    avg = 0
    list2 = []

    for num in list:
        avg += num
    avg = avg//len(list)

    for num in list:
        if num > avg:
            list2.append(num)

    print(list2)

greaterThanAverage()

