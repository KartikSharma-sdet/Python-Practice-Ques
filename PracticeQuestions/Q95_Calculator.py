import Input_Keywords.input as input

# From Jenny's Lectures

def calculator():

    check = "yes"
    result = 0
    num1 = 0
    num2 = 0
    operation = 0
    operator = ""
    count = 0

    while(check == "yes"):

        if count == 0:
            num1 = input.inputInteger()
            count = 1
        else :
            num1 = result
        print("Choose Operation :")
        print("Type 1 for addition, +")
        print("Type 2 for subtraction, -")
        print("Type 3 for multiplication, *")
        print("Type 4 for division, //")
        print("Type 5 for power, **")
        operation = input.inputInteger()
        num2 = input.inputInteger()

        if operation == 1:
            result = num1 + num2
            operator = "+"
        elif operation == 2:
            result = num1 - num2
            operator = "-"
        elif operation == 3:
            result = num1 * num2
            operator = "*"
        elif operation == 4:
            result = num1 // num2
            operator = "//"
        elif operation == 5:
            result = num1 ** num2
            operator = "**"

        print(f"{num1} {operator} {num2} = {result}")

        print(f"Do you want to continue with performing operations on {result} or close calculator ? Enter 'yes' or 'no'")
        check = input.inputString()

    print(f"Your final result is : {num1} {operator} {num2} = {result}")

calculator()
