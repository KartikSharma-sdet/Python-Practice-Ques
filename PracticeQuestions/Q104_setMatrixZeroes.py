import Input_Keywords.input as input

# Set Matrix Zeroes
# If an element is 0, set its entire row and column to 0.

def setMatrixZeroes():

    print("input rows for a 3x3 matrix")
    list1 = input.inputListWithoutLength(3)
    list2 = input.inputListWithoutLength(3)
    list3 = input.inputListWithoutLength(3)

    zero = []

    matrix = [list1, list2, list3]

    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                zero.append([i,j])

    for k in zero:
        for a in range(3):
            matrix[k[0]][a] = 0
            matrix[a][k[1]] = 0

    print(matrix)

setMatrixZeroes()
