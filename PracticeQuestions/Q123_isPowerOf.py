import Input_Keywords.input as input

def isPowerOf():

    print("Enter the number")
    n = input.inputInteger()
    print("enter the base to divide the number by")
    base = input.inputInteger()

    if n < 1:
        return False

    while n % base == 0:
        n = n//base

    return n == 1

bool1 = isPowerOf()

print(bool1)