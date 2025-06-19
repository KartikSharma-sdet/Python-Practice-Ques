import Input_Keywords.input as input

# Print a pascal's triangle

# Input
# Enter the number of levels
# Enter any Number : 5

# Output
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

def printPascalTriangle():

    print("Enter the number of levels")
    levels = input.inputInteger()

    pascal = [[1], [1,1]]

    for i in range(2, levels):
        temp = []
        for j in range(0, i):
            if j == 0:
                temp.append(1)
            else:
                temp.append(pascal[i-1][j-1] + pascal[i-1][j])
        temp.append(1)

        pascal.append(temp)

    j = 1
    for row in pascal:
        for space in range(levels-1-j, -1,-1):
            print(end=" ")
        j += 1
        for num in row:
            print(num, end=" ")
        print()


printPascalTriangle()

