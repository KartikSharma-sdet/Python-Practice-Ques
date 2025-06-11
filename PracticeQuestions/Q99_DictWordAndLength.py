import Input_Keywords.input as input

# Input words as keys of the dictionary and their length as their respective values

def wordsAndTheirLengths():

    length = input.inputLength()
    dict1 = {}

    for i in range(length):
        s = input.inputString()
        dict1[s] = len(s)

    print(dict1)

wordsAndTheirLengths()

