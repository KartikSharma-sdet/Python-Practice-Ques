import Input_Keywords.input as input

#   *
#  ***
# *****

def pyramidPattern():

    levels = input.inputInteger()

    for i in range(0, levels+1):

        for j in range(0, (levels -i)):
            print(" ", end="")

        length = (i*2)-1

        for j in range(length):
            print("*", end="")
        print()

pyramidPattern()