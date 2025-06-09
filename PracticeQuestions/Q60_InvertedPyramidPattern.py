import Input_Keywords.input as input

# input : 6
# output :
#
# ***********
#  *********
#   *******
#    *****
#     ***
#      *

def invertedPyramidPattern():

    levels = input.inputInteger()-1

    for i in range(levels+1, 0, -1):

        for j in range(0, (levels -i)+1):
            print(" ", end="")

        length = (i*2)-1
        for j in range(length):
            print("*", end="")
        print()

invertedPyramidPattern()