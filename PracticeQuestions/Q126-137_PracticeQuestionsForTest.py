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


def printOccurance():
    list1 = [1, 2, 4, 2, 3, 1, 6]
    dict1 = {}

    for element in list1:
        if element in dict1.keys():
            dict1[element] += 1
        else:
            dict1[element] = 1
    print(dict1)


printOccurance()

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

# Print All Digits of a Number in Reverse Order (One per Line)

def printAllDigitsInReverse():

    num = input.inputInteger()
    n = num

    while n > 0:
        temp = n%10
        n = n//10
        print(temp)

printAllDigitsInReverse()

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

# Print All Digits of a Number in Reverse Order (One per Line)



def Q6divBy3And5():

    for i in range(101):
        if i % 3 == 0 and i % 5 == 0:
            if i % 30 != 0:
                print(i)

print(ord("0"), ord("9"), ord("A"), ord("Z"), ord("a"), ord("z"))


def first100NumbersWithoutLoop(n):
    if n<100:
        print(n, end=" ")
    else : return

    first100NumbersWithoutLoop(n+1)


# list(map(print, range(1, 101)))

# s = "fedcba"
# s1 = s[::-1]
#
# print(s1)

def first100NumberInReverse(n):
    if n > 100:
        return
    first100NumberInReverse(n+1)
    print(n)

def joinFunction():
    string = input.inputString()

    list = string.split(" ")

    newString = "-".join(list)

    print(newString)

string = "abcdef"

print(string.join(["1","2","3","4","5","6"]))


#  Count Characters Without Using len()

def length():

    s = input.inputString()
    count = 0

    for char in s:
        count += 1

    print(count)

