import Input_Keywords.input as input

# Merge Two Dictionaries and Sum Values of Common Keys

def mergeTwoDictionaries():

    length = input.inputLength()

    dict1 = input.inputDictionary(length)
    dict2 = input.inputDictionary(length)

    dict_final = {}

    for key in dict1.keys():
        dict_final[key] = int(dict1[key])

    for key in dict2.keys():
        if key in dict_final.keys():
            dict_final[key] += int(dict2[key])
        else :
            dict_final[key] = int(dict2[key])

    print(dict_final)

mergeTwoDictionaries()