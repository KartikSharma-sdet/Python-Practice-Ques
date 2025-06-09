import Input_Keywords.input as input

# Find the number of even digits inside a given number

def evenDigits():

    number = input.inputInteger()
    list = []

    for dig in str(number):
        digit = int(dig)
        if digit%2 == 0:
            list.append(digit)

    print(f"There are {len(list)} even digits, {list}")

evenDigits()

