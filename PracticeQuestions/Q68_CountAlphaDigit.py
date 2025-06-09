import Input_Keywords.input as input

# input : Enter any string : abcdefgh2.3.4'5'6.7=9
# output : There are 8 alphabets, 7 digits and 6 special characters in abcdefgh2.3.4'5'6.7=9

def countAlphabetsAndDigitsAndSpecial():

    string = input.inputString()

    countAlpha = 0
    countDigit = 0
    countSpecial = 0

    for char in string:

        if 'a' <= char.lower() <= 'z':
            countAlpha += 1
        elif '0' <= char <= '9':
            countDigit += 1
        else:
            countSpecial += 1

    print(f"There are {countAlpha} alphabets, {countDigit} digits and {countSpecial} special characters in {string}")

countAlphabetsAndDigitsAndSpecial()
