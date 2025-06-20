import Input_Keywords.input as input

# TEST QUESTIONS

# Q1. Input list and leave unique number only in a duplicated list
# Q2. count the number of times each element appears
# Q3. OOPs concepts for area of square, circle, triangle, rectangle
# Q4. Reverse the sentence but not the characters of its words
# Q5. find the word in a sentence which has a digit in it .

# Ans 1

def  uniqueOnly():

    list = input.inputList()
    result = []
    for num in list:

        if num in result :
            continue
        else:
            result.append(num)
    print(result)

# Ans 2

def timesEachElementAppears():

    string = input.inputString()
    dict = {}

    for char in string:
        if  char in dict.keys():
            dict[char] += 1
        else:
            dict[char] = 1

    print(dict)

# Ans 3

class Circle:
     def __init__(self, radius):
         self.radius = radius

     def area(self):
         self.area = 3.14 * (self.radius ** 2)
         print(self.area)

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        self.area = self.side ** 2
        print(self.area)

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        self.area = self.length * self.breadth
        print(self.area)

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        self.area = 0.5 * self.height * self.base
        print(self.area)

# circle1 = Circle(2)
#
# circle1.area()

# Ans 4

def reverseSentenceNotWords():

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

    for i in range(len(list) - 1, -1, -1):
        newS += list[i] + " "

    print(newS)


# Ans 5

def findTheWordWithDigit():

    s = input.inputString()

    list = s.split(" ")
    temp = ""

    for word in list:
        for char in word:
            if ord(char) >= 48 and ord(char) <= 57 and temp == "":
                temp = word

    print(temp)

findTheWordWithDigit()

# Practice Questions

def findDigitsMoreThanOnce():

    num = input.inputInteger()
    string = str(num)
    list = []
    res = []

    for char in string:
        if char in list:
            res.append(char)
        else:
            list.append(char)

    print(res)

def twoSum():

    list = input.inputList()
    print("Give the target sum")
    target = input.inputInteger()

    for num in list:
        temp = target-num
        if temp in list:
            return True

    return False

def firstPrimeNumbers(n):

    # n = input.inputInteger()
    temp = 2
    count = 0
    list = []
    counter = True

    while count < n :
        for i in range(2, temp):
            if temp%i == 0:
                counter = False
                break
        if counter == True:
            list.append(temp)
            count += 1
        temp += 1
        counter = True

    return list

def triangleOfPrimeNumbers():

    print("Enter the levels of the triangle")
    levels = input.inputInteger()
    n = 0
    for i in range(levels+1):
        n += i
    letcount = 0

    Primelist = firstPrimeNumbers(n)


    for level in range (1, levels+1):
        for j in range(1, level+1):
            print(Primelist[letcount], end = " ")
            letcount += 1
        print()


def reverseWordInSentenceWithoutUsingSplit():

    string = input.inputString()

    list = []
    result = ""
    temp = ""

    for char in string:
        if(char == " "):
            list.append(temp)
            temp = ""
            continue
        temp += char
    list.append(temp)

    for word in list:
        temp = ""
        for i in range(len(word)-1, -1, -1):
            temp += word[i]
        result += temp
        result += " "

    print(result)

def isNumPalindrome():

    num = input.inputInteger()
    n = num
    res = 0

    while n > 0:
        temp = n%10
        res = res*10 + temp
        n = n//10

    print(f"num is {num}, reverse is {res} , {res == num}")

def rotateAListBykSteps():

    list = input.inputList()
    print("Enter the steps")
    k = input.inputInteger()
    res = []

    for i in range(len(list)-k,len(list) ):
        res.append(list[i])

    for i in range(len(list)-k):
        res.append(list[i])

    print(res)
