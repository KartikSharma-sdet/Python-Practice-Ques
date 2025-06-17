import Input_Keywords.input as input


def findDuplicates():

    string = input.inputString()

    duplicates = []
    list = []

    for char in string:
        if char in list:
            duplicates.append(char)
        else:
            list.append(char)

    print(duplicates)

findDuplicates()