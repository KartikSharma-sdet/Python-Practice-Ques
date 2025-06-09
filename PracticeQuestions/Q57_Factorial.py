import Input_Keywords.input as input

def factorial(num) -> int:

    # num = input.inputInteger()
    fact = 1

    for i in range(2,num+1):

        fact *= i

    return fact

# num2 = factorial(5)
# print(num2)
