import Input_Keywords.input as input

# Remove those keys from a dictionary which have no values.

def  removeEmptyValues():

    length = input.inputLength()
    dict1 = input.inputDictionary(length)
    dict2 = {}

    for key in dict1.keys():
        if dict1[key] != '':
            dict2[key] = dict1[key]

    print(dict2)



removeEmptyValues()

