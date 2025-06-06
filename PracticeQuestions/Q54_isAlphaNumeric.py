import Input_Keywords.input as input

# Check for alphanumeric strings
# input = "abc23876as"
#  output = true

def AlphaNumeric():

    string = input.inputString()
    count = 0
    character = 0
    number = 0

    for char in string:

        if char >= 'a' and char <= 'z' :
            character = 1
        elif char >= 'A' and char <= 'B' :
            character = 1
        elif char >= '0' and char <= '9':
            number = 1
        elif number == 1 and character == 1:
            print(f"{string} is alphanumeric")
            break

    if number == 1 and character == 1:
         print(f"{string} is alphanumeric")
    else :
         print(f"{string} is not alphanumeric")

AlphaNumeric()