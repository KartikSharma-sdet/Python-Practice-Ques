import Input_Keywords.input as input

def decimalToBinary():

    decimalNum = input.inputInteger()

    binaryNum = ""

    if decimalNum == 0:
        print("0")
        return "0"

    while decimalNum > 0:
        bit = decimalNum % 2
        binaryNum = str(bit) + binaryNum
        decimalNum = decimalNum//2

    print(binaryNum)

decimalToBinary()