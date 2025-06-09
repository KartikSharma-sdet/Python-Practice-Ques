import Input_Keywords.input as input

def printPairsWithGivenSum():

    list = input.inputList()
    targetSum = input.inputInteger()
    count = 0

    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            num = list[j]
            sum = list[i] + num
            if sum == targetSum:
                count += 1
                print(f"({list[i]}, {num})")

    if count == 0:
        print("No pairs found")

printPairsWithGivenSum()