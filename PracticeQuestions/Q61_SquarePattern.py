import Input_Keywords.input as input

# input : 5
#
# output :
#
# *  *  *  *  *
# *           *
# *           *
# *           *
# *  *  *  *  *

def printSquareStarPattern():

    levels = input.inputInteger()

    for i in range(0, levels):

        if i == 0 or i == (levels-1):
            for j in range(0, levels):
                print("*", end = "")
                print("  ", end="")
        else:
            for j in range(0, levels):
                if j == 0 or j == (levels-1):
                    if j == (levels-1):
                        print("  ", end="")
                    print("*", end = "")
                else :
                    print("   ", end = "")

        print()

printSquareStarPattern()