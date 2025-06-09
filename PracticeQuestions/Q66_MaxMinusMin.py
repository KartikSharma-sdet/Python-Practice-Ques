import Input_Keywords.input as input

# Locate the maximum and minimum element within a list and print their difference

def maxMinusMin():

    list = input.inputList()
    min = list[0]
    max = list[0]

    for num in list:

        if num < min:
            min = num

        if num > max:
            max = num

    print(f"The difference between max({max}) and min({min}) is {max - min}")

maxMinusMin()