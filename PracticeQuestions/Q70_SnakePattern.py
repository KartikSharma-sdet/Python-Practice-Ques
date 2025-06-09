import Input_Keywords.input as input

# input : Enter any Number : 3
# output :
# 1 2 3  ->
# 6 5 4  <-
# 7 8 9  ->

def snakePattern():

    levels = input.inputInteger()

    row = []
    count = 0

    for i in range(0, levels):

        for j in range(3):
            count += 1
            row.append(count)

        if i%2 == 0:
            for num in row:
                print(num, end=" ")
        else:
            for k in range(2,-1,-1):
                num = row[k]
                print(num, end=" ")

        print()
        row = []

snakePattern()
