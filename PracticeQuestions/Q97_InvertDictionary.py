import Input_Keywords.input as input

# swapping keys with values

def invertDictionary():

    length  = input.inputLength()
    dict1 = input.inputDictionary(length)
    dict2 = {}

    for key in dict1.keys():
        value = dict1[key]
        dict2[value] = key

    print(dict2)

invertDictionary()