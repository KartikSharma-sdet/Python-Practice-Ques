import Input_Keywords.input as input

# Sort a dictionary using bubble sort

def sortDictionary():

    length = input.inputLength()
    dict1 = input.inputDictionary(length)

    itemsList = list(dict1.items())

    for i in range(0, len(itemsList)):

        for j in range(i+1, len(itemsList)):
            if itemsList[i][1] > itemsList[j][1]:
                temp = itemsList[i]
                itemsList[i] = itemsList[j]
                itemsList[j] = temp

    print(dict(itemsList))

sortDictionary()