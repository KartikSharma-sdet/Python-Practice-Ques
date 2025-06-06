import Input_Keywords.input as input

#    A
#   BBB
#  CCCCC
# DDDDDDD
#EEEEEEEEE

def pyramidPatternWithAlphabet():
    levels = input.inputLength()

    for i in range(1, levels+1):
        for j in range(0, (levels -i)):
            print(" ", end="")

        length = (i*2)-1
        for j in range(length):
            print(chr(64+i), end="")

        print()

pyramidPatternWithAlphabet()