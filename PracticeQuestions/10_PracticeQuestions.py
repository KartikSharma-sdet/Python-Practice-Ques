import Input_Keywords.input as input

def Q1reverseWordsInAString():

    string = input.inputString()

    list = []
    temp = ""

    for char in string:
        if char == " ":
            list.append(temp)
            temp = ""
            continue
        temp += char
    list.append(temp)

    newS = ""

    for i in range(len(list)-1, -1, -1):
        newS += list[i] + " "

    print(newS)

def Q2count7():

    n = input.inputInteger() + 1
    count = 0

    for i in range(1, n):
        temp = str(i)
        for char in temp:
            if int(char) == 7:
                count += 1

    print(count)

def Q3firstNonRepeatingChar():

    string = input.inputString()
    dict = {}

    result = -1

    for char in string:
        if char in dict.keys():
            dict[char] += 1
        else :
            dict[char] = 1

    for key in dict:
        if dict[key] == 1:
            result = key
            break

    print(result)

def Q4isPalindrome():

    string = input.inputString()
    newS1 = ""
    newS2 = ""

    for char in string:
        if char == " ":
            continue
        newS1 += char.lower()

    for i in range(len(newS1)-1, -1, -1):
        newS2 += newS1[i]

    print(newS1 == newS2)

def Q5swapFirstAndLast():

    list = input.inputList()

    list[0],list[len(list)-1] = list[len(list)-1], list[0]

    print(list)


def Q7removeDuplicates():

    list = input.inputList()

    list2 = []

    for num in list:
        if num in list2:
            continue
        else:
            list2.append(num)

    print(list2)

def Q9sumOfDigits():

    number = input.inputInteger()

    sum = 0

    for dig in str(number):
       sum += int(dig)

    while(len(str(sum))>1):
        temp = 0
        for dig in str(sum):
            temp += int(dig)
        sum = temp

    print(sum)


def Q10secondMax():

    list = input.inputList()
    max = list[0]
    max2 = list[0]

    for num in list:

        if num > max:
            max2 = max
            max = num
        elif num > max2 and num < max:
            max2 = num

    print(max2)


def Q6divBy3And5():

    for i in range(101):
        if i % 3 == 0 and i % 5 == 0:
            if i % 30 != 0:
                print(i)


def Q8rotatedList():

    length = input.inputLength()
    list1 = input.inputListWithoutLength(length)
    list2 = input.inputListWithoutLength(length)
    listNew = []

    start = list2.index(list1[0])

    for i in range(start, len(list2)):
        listNew.append(list2[i])

    for i in range(0, start):
        listNew.append(list2[i])

    print(list1)
    print(list2)
    print(listNew)
    print(list1 == listNew)

