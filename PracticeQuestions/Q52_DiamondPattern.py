import Input_Keywords.input as input

def diamondPattern():

    levels = input.inputLength()

    for i in range(0, levels + 1):

        for j in range(0, (levels - i)):
            print(" ", end="")

        length = (i * 2) - 1

        for j in range(length):
            print("*", end="")
        print()

    for i in range(levels-1, -1, -1):

        for j in range((i-levels)-1, -1):
            print(" ", end="")

        length = (i*2)-1

        for j in range(length):
            print("*", end="")
        print()

diamondPattern()