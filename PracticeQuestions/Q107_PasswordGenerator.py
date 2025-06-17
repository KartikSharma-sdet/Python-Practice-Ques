import Input_Keywords.input as input

# Password Generator

import random

def passwordGenerator():

    length = input.inputInteger()

    uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercaseLetters = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    symbols = "!@#$%^&*"

    all_chars = uppercaseLetters + lowercaseLetters + digits + symbols
    password = ""

    for i in range(length):
        index = random.randint(0, len(all_chars) - 1)
        password += all_chars[index]

    print(password)

passwordGenerator()
