import Input_Keywords.input as input

def stringToInteger():
    string = input.inputString()
    result = 0

    for char in string:
        digit = ord(char) - ord('0')
        result = (result * 10) + digit

    print(result)

stringToInteger()
