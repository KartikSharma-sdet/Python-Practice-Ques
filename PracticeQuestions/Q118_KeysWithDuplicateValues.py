import Input_Keywords.input as input

def keysWithDuplicateValues():
    length = input.inputLength()
    dict1 = input.inputDictionary(length)

    values = {}

    for value in dict1.values():
        if value in values:
            values[value] += 1
        else:
            values[value] = 1

    list1 = []

    for key in dict1.keys():
        value = dict1[key]
        if values[value] > 1:
            list1.append(key)

    print(list1)
keysWithDuplicateValues()