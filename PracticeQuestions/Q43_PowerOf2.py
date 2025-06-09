import Input_Keywords.input as input

# Check if a Number is a Power of 2


def poweroftwo():

    num = input.inputInteger()
    n = num

    while n > 1:
        if n%2 == 0:
            n = n/2
        else: break

    if n == 1:
        print("True")
    else:
        print("False")

poweroftwo()