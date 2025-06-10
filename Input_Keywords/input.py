
def inputList() -> list:
    length = int(input("Enter the length of the list : "))

    list = []

    for i in range(length):
        temp = int(input(f"Enter index {i} element for the list : "))
        list.append(temp)
    return list

def inputString() -> str:

    String = input("Enter any string : ")
    return String

def inputInteger() -> int:

    Number = int(input("Enter any Number : "))
    return Number

def inputEmptySet() -> set:
    set1 = set()
    return set

def inputSet() -> set:
    length = int(input("Enter the length of the set : "))

    set = set()

    for i in range(length):
        temp = int(input(f"Enter index {i} element for the list : "))
        set.add(temp)
    return set

def inputListWithoutLength(length) -> list:
    list = []

    for i in range(0, length):
        temp = int(input(f"Enter index {i} element for the list : "))
        list.append(temp)
    return list

def inputLength() -> int:
    length = int(input("Enter length : "))

    return length

def encrypt_decrypt() -> str:
    String = input("What to do ? : encrypt or decrypt : ")
    return String

def inputFloat() -> float:
    flt = float(input("Enter any float value: "))
    return flt

def inputListOfString() -> list:
    length = int(input("Enter the length of the list : "))

    list = []

    for i in range(length):
        temp = input(f"Enter index {i} element for the list : ")
        list.append(temp)
    return list

def inputJewelsAndStones() -> int:

    jewels = input("Enter the Jewels : ")
    stones = input("Enter the Stones : " )

    return jewels,stones

def inputDictionary(length) -> dict:

    dict = {}

    for i in range(0, length):
        key = input(f"Enter key for index {i} pair: ")
        value = input(f"Enter value for index {i} pair: ")
        dict[key] = value

    return dict

def inputSentence() -> str :

    s = input("Enter a sentence : ")

    return s

def inputName() -> str :

    s = input("Enter a name : ")

    return s

def inputBid() -> int :

    s = int(input("Enter a bid : "))

    return s

def inputYesOrNo() -> str:

    check = input("Enter 'yes' or 'no' : ")
    return check

