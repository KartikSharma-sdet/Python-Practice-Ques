import math

import Input_Keywords.input as input

# Prime Number Checker (Range)
# Ask the user to input a number n. Print all prime numbers from 1 to n using a loop.

def primeNumber():
    num = input.inputInteger()
    count = 0

    if num <= 1 :
        print(f"{num} is not a prime number")
        count = 1
    else:
        for i in range(2, (int(math.sqrt(num))+1)):
            if num%i == 0:
                print(f"{num} is not a prime number")
                count = 1
                break
    if count == 0:
        print(f"{num} is a prime number")

primeNumber()