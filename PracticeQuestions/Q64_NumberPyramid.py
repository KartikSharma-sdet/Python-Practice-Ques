import Input_Keywords.input as input

# input : 3
# output :
#
# 1
# 2 3 4
# 5 6 7 8 9

def NumberPyramidPattern():
    levels = input.inputInteger()
    count = 1

    for i in range(0, levels + 1):

        if count > 10:
            temp = i-1
        else:
            temp = i

        for j in range(0, temp):
            print(count, end=" ")
            count += 1
        print("")

NumberPyramidPattern()