import Input_Keywords.input as input
import Q57_Factorial as fact

# Check if a Number is a Strong Number
# A Strong number is one in which the sum of factorials of each digit equals the number itself.

def strongNumber():

    num = input.inputInteger()
    temp = num
    result = 0

    while temp > 0:
        digit = temp % 10
        result += fact.factorial(digit)
        temp //= 10

    if result == num:
        print("True")
    else :
        print("False")

strongNumber()


