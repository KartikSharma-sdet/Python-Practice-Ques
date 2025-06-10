import Input_Keywords.input as input

# input : abcdeabcd
# output : e

def removeDuplicates():

    s = input.inputString()
    new = ""
    list = []

    for char in s:
        if char not in list:
            list.append(char)
        elif char in list:
          list.pop(list.index(char))

    for char in list:
        new+= char
    print(new)

removeDuplicates()