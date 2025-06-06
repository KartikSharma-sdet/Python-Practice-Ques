import Input_Keywords.input as input

# Even and Odd Splitter
# Ask the user to input a list of 10 numbers. Separate them into even and odd lists, and print both.

def EvenOddSplitter():

    list = input.inputList()

    even = []
    odd = []

    for num in list:
        if num%2 == 0:
            even.append(num)
        else:
            odd.append(num)

    print(f"Even numbers are {even}")
    print(f"Odd numbers are {odd}")

EvenOddSplitter()