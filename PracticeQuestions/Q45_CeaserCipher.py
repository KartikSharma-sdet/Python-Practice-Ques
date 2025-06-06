import Input_Keywords.input as input
# Input
# Enter any string : abcdef
# Shift Number : 2
# what to do ? : encrypt or decrypt : encrypt
# Output
# cdefgh

def CeaserCipher():

    string = input.inputString()
    shift_number = input.inputInteger()
    choose = input.encrypt_decrypt()
    string = string.lower()

    if choose == 'encrypt':
        string_new = encrypt(shift_number, string)
    else :
        string_new = decrypt(shift_number, string)

    print(string_new)

def encrypt(shift_number, string) -> str:
    string_new = ""

    for char in string:
        temp = int(ord(char) + shift_number)
        if temp > 122 :
            temp = 96 + (temp-122)
        string_new += chr(temp)

    return string_new

def decrypt(shift_number, string) -> str:
    string_new = ""

    for char in string:
        temp = int(ord(char) - shift_number)
        if temp <97 :
            temp = 122 - (96-temp)
        string_new += chr(temp)
    return string_new


CeaserCipher()