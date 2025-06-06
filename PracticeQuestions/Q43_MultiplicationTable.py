import Input_Keywords.input as input

def multiplicationTable():

    number = input.inputInteger()

    for i in range(10):
        print(f"{number} x {i+1} = {number*(i+1)}")

multiplicationTable()