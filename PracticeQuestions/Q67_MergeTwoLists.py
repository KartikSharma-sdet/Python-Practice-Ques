import Input_Keywords.input as input

def mergeTwoSortedLists():

    length = input.inputLength()

    list1 = input.inputListWithoutLength(length)
    list2 = input.inputListWithoutLength(length)
    list3 = []

    i = 0
    j = 0

    while(i < length and j <length):


        num1 = list1[i]
        num2 = list2[j]

        if(num1<num2):
            list3.append(num1)
            i += 1
        else:
            list3.append(num2)
            j += 1


    if i < length:
        list3 += list1[i:]
    elif j < length:
        list3 += list2[j:]

    print(list3)

mergeTwoSortedLists()