import Input_Keywords.input as input

# input = 1559

# output = 1 + 5 + 5 + 9 = 20

def sumOfDigits():

    string = str(input.inputInteger())
    sum = 0

    for digit in string:
        sum += int(digit)

    print(sum)

sumOfDigits()
