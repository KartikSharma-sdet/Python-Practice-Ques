import Input_Keywords.input as input

# input = "abCDef"
# output = "ABcdEF"

def toggleCase():

    string = input.inputString()
    new_string = ""

    for char in string:

        if ord(char) >= ord('A') and ord(char) <= ord('Z'):
            new_string += chr(ord(char) + 32)
        elif ord(char) >= ord('a') and ord(char) <= ord('z'):
            new_string += chr(ord(char) - 32)
        else :
            new_string += char

    print(new_string)

toggleCase()
