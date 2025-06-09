def fibonacci() :
    target = input("Enter the final number : ")
    print(type(float(target)))

    if(target.isdigit()):
        a = 0
        b = 1
        c = 0
        print(a)
        target = int(target)

        i = 1

        while (i < target):
            c = a + b
            a = b
            b = c
            print(a)
            i += 1
    elif (target.isalpha()):
        print(f"You have entered {target} which is an alphabet, please enter a number")
    else :
        print(f"You have entered {target} which is a special character or a decimal, please enter a number")



def func1():
    str = input("Enter any string : ")
    list = [1,2,3,4,5]

    for char in str :
        print(char)

def func2():

    length = int(input("Enter the number of elements in the list : "))
    list = []
    sum = 0

    for i in range(0,length):
        temp = int(input(f"Enter place {i+1} integer : "))
        list.append(temp)
        sum += temp

    print(round(sum/length))

def func3():

    length = int(input("Enter the number of elements in the list : "))
    list = []
    max = 0

    for i in range(0, length):
        temp = int(input(f"Enter place {i + 1} integer : "))
        list.append(temp)
        if(temp>max):
            max = temp

    print(max)

def func4() :

    length = int(input("Enter the last number : ")) + 1;
    sum = 0

    for i in range(2, length, 2):
        sum += i

    print(sum)

def func5FuzzBizz() :

    l = int(input("Enter the last number : "))

    for i in range(1,l+1):

        if i%3 == 0 and i%5 == 0 :
            print("FizzBuzz")
        elif i%3 == 0 :
            print("Fizz")
        elif i%5 == 0 :
            print("Buzz")
        else : print(i)

def func6_leet1_twoSum():

    list = [2, 7, 11, 5]
    target = 7
    temp = 0

    for i in range(0, len(list)):
        temp = target-list[i]
        if(list.__contains__(temp)):
            print([i, list.index(temp)])
        break

def func7_leet136_singleNumber():

    list = [1, 2, 1, 3, 5, 3, 4, 4, 5]
    target = 0

    for num in list:
        target = target^num

    print(target)

def func8_leet125_validPalindrome():

    string = input("Enter any string : ")
    last = -1
    count = 0
    length = len(string)

    for i in range(0, length//2):
        if string[last] != string[i]:
            print("Not a Palindrome")
            count += 1
            break
        last -= 1

    if count == 0 :
        print("Palindrome")


def func9_leet258_addDigits():
    number = input("Enter any number : ")
    sum = 0

    if len(number) > 1 :

        for dig in number:
            sum += int(dig)
    else : print(number)

    if len(str(sum)) >  1:
        temp = 0
        for dig in str(sum):
            temp += int(dig)

        print(temp)
    else: print(sum)


def func10_leet371_sumOfTwoIntegers():

    num1 = int(input("Enter any number : "))
    num2 = int(input("Enter any number : "))

    sum = num1 ^ num2

    print(sum)

def func11_leet461_hamming_distance():

    num1 = int(input("Enter any number : "))
    num2 = int(input("Enter any number : "))

    temp = num1 ^ num2
    count = 0
    result = bin(temp).replace("0b", "")

    for i in str(result) :
        if i == "1" :
            count += 1
    print(count)

def func12_leet191_hammingWeight():

    num1 = int(input("Enter any number : "))
    count = 0

    binaryNum = bin(num1).replace("0b","")

    for i in binaryNum :
        if(i == "1"):
            count += 1

    print(count)

def func13_sumOfSquares(num) -> int :
    sum = 0
    for i in str(num) :
        sum += int(i)**2
    print(sum)
    return sum


def func14_leet202_happyNumber() -> bool:

    n = int(input("Enter any number : "))
    visit = set()

    while n not in visit:
        visit.add(n)
        n = func13_sumOfSquares(n)

        if(n == 1):
            print("True")
            break

    if n != 1 :
        print("False")


def func15_leet231_powerOfTwo():
    n = int(input("Enter any number : "))

    while(n%2 == 0):
        n = n/2
        if(n == 1):
            print("true")

    if(n != 1):
        print("false")

def func16_leet709_toLowerCase():
    string = input("Enter any string : ")
    i = 0
    new_string=""

    for char in string:
        temp = ""
        if(ord(char) >= 65 and ord(char)<=90):
            temp += chr(ord(char) + 32)
        else : temp += char
        i += 1
        new_string += temp
    print(new_string)

def func17_leet520_detectCapital():

    string = input("Enter any string : ")
    count = 0

    if(ord(string[0]) > 95):
        for char in string:
            if(ord(char) <= 95):
                print("Unsuccessful")
                count+=1
                break

        if count == 0:
            print("Successful")

    elif(ord(string[1]) <= 95):
        for char in string :
            if(ord(char) > 95):
                print("Unsuccessful")
                count += 1
                break
        if count == 0:
            print("Successful")
    else:
        for i in range(1, len(string)):
            if(ord(string[i]) <= 95):
                print("Unsuccessful")
                count += 1
                break
        if count == 0:
            print("Successful")


def func18_leet242_validAnagram():

    string1 = input("Enter 1st string : ")
    string2 = input("Enter 2nd String : ")
    count = 0

    set1 = []

    for char in string1 :
        set1.append(char)

    for char in string2 :
        count += 1
        if(set1.__contains__(char)):
            continue
        else :
            print(f"${string1} and ${string2} are not Anagrams")
    if(count == len(string1)):
        print(f"{string1} and {string2} are Anagrams")
    else : print(f"{string1} and {string2} are not Anagrams")

def func19_leet414_ThirdMaximumNumber ():

    list = [1, 2, 3, 4,5 ,6 ,7 ,8 ,9, 10]

    list.sort()

    print(list[len(list)-3])

def func20_leet1295_numbersWithEvenNumberOfDigits():

    list = [12, 134, 1424, 1232, 12, 132, 1 ,4 ,6]
    count = 0

    for num in list:
        if(len(str(num)) % 2 == 0 ):
            count += 1

    print(f"{count} out of {len(list)} are numbers with even digits")

def func21_MaxSumOfThreeNumbers():

    list = [1, 2, 3, 4, 5, 10, 11, 12, 8]

    sum = 0
    list.sort()

    for i in range(len(list)-3, len(list)):
        sum += list[i]

    print(sum)

def func22_leet628_MaxProductOfThreeNumbers():
    list = [1, 2, 3, 4, 5, 10, 11, 100, 8]

    prod = 1

    list.sort()

    for i in range(len(list)-3, len(list)):
        prod *= list[i]

    print(prod)

def func23_leet697_degreeOfAnArray():
    list = [1, 2, 2, 3, 4, 5, 6,6,6, 7]
    max = 0
    num = 0

    set1 = set()

    for num in list:
        set1.add(num)

    for dig in set1:
        temp = 0
        temp = list.count(dig)
        if(temp>max):
            num = dig
            max = temp

    print(f"{num} has occurred {max} times ")

def func24_leet344_reverseString():

    string = input("Enter any string : ")

    new_string = ""

    for i in range(-1, -len(string)-1, -1):
        new_string += string[i]

    print(new_string)


def func25_leet349_IntersectionOfTwoArrays():

    list1 = [1, 2, 3, 4, 5, 2]
    list2 = [2, 2, 5, 5, 7 , 8 ,9]
    list_new=[]

    for num in list1:
        if(list2.__contains__(num)):
            if(list_new.__contains__(num)):
                print()
            else: list_new.append(num)

    print(list_new)

def func26_leet268_missingNumber():

    length = int(input("Enter the number of items inside list : "))

    list = []
    list2 = []

    for i in range(0,length):
        temp = int(input(f"Enter number {i} element for list : "))
        list.append(temp)
        list2.append(i)

    list.sort()

    print(list.__eq__(list2))


def func27_leet287_findTheDuplicateNumber():
    length = int(input("Enter the number of items inside list : "))
    list = []
    set1 = set()

    for i in range(0, length):
        temp = input(f"Enter number {i} element for list : ")
        list.append(temp)

    for num in list:
        if set1.issuperset(num) :
            print(num)
            break
        else :
            set1.add(num)

def inputList() -> list:
    length = int(input("Enter the length of the list : "))

    list = []

    for i in range(length):
        temp = int(input(f"Enter index {i} element for the list : "))
        list.append(temp)
    return list

def func28_leet21_removeDuplicatesFromSortedList():

    list = inputList()

    i = 0
    j = 1

    while(j<len(list)):

        if list[i] != list[j] :
            i += 1
            list[i] = list[j]

        j += 1

    print(list[0:i+1])


def func29_leet27_removeElement() :
    list = inputList()
    target = int(input("Enter the number to be removed : "))

    i = 0
    j = 1

    while (j < len(list)):

        if list[j] != target:
            i += 1
            list[i] = list[j]

        j += 1

    print(list[0:i + 1])

def func30_leet35_searchInsertPosition():

    list = inputList()
    target = int(input("Enter the number to be added : "))
    count = 0

    for i in range(0, len(list)):
        temp = list[i]

        if(temp == target):
            print(f"{i} is the index at which {target} is found")
            count = 1
        if(temp > target):
            print(f"{i} is the index at which {target} should be added")
            count = 1
            break


    if count == 0:
        print(f"{i+1} is the index at which {target} should be added")




