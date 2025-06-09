import Input_Keywords.input as input

# Find the product of digits of a number
# input : 12345
# output : 120

def productOfDigits():

    num = input.inputInteger()
    prod = 1

    for dig in str(num):

        prod *= (int(dig))

    print(f"Product of digits of {num} is {prod}")

productOfDigits()