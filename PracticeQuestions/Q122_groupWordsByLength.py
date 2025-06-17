import Input_Keywords.input as input

def groupWordsByLength():

    string = input.inputString()
    list = string.split(" ")
    result = {}

    for word in list:
        length = len(word)
        if length in result:
            result[length].append(word)
        else:
            result[length] = [word]

    print(result)

groupWordsByLength()

