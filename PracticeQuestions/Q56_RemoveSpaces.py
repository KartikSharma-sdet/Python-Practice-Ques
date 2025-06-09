import Input_Keywords.input as input

# input = " I am a boy "
# output = "Iamaboy"



def removeSpacesFromAString():

    string = input.inputString()
    new = ""

    for char in string :
        if char != " ":
            new += char

    print(new)

removeSpacesFromAString()