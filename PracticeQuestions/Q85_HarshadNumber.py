import Input_Keywords.input as input

# Enter any Number : 18
# 1 + 8 = 9, 18%9 == 0 , thus it is a harshad number
# 18 is a harshad number

def isHarshadNumber():

    num = input.inputInteger()
    sum = 0

    for dig in str(num):
        sum += int(dig)

    if num%sum == 0:
        print(f"{num} is a harshad number")
    else:
        print(f"{num} is not a harshad number")

isHarshadNumber()