import  Input_Keywords.input as input

# *
# **
# ***
# ****
# *****

def pyramidPatternNoSpaces():

    levels = input.inputInteger()

    for i in range(0, levels+1):
        for j in range(0, i):
            print("*", end="")
        print("")

pyramidPatternNoSpaces()

