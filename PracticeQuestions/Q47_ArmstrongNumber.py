import Input_Keywords.input as input

# An Armstrong number is a number that is equal to the sum of the cubes of its digits (for 3-digit numbers).
#
# For example:
# 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153

def isArmstrong():

    number = input.inputInteger()
    sum = 0

    for dig in str(number):
        sum += int(dig)**3

    if number == sum:
        print(f"Yes, {number} is an armstrong number")
    else:
        print(f"No, {number} is not an armstrong number")

isArmstrong()
