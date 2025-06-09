import Input_Keywords.input as input

# 1572. Matrix Diagonal Sum
# Given a square matrix mat, return the sum of the matrix diagonals.
#
# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
#
# Example 1:
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25

def matrixDiagonalSum():

    list1 = input.inputListWithoutLength(3)
    list2 = input.inputListWithoutLength(3)
    list3 = input.inputListWithoutLength(3)

    matrix = [list1, list2, list3]
    length = len(matrix)-1
    sum = 0

    for i in range(0, length+1):
        sum += matrix[i][i]

        if i != (length-i):
            sum += matrix[i][length-i]
    print(f"Sum of all the diagonal elements is {sum}")

matrixDiagonalSum()

