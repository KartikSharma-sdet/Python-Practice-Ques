import Input_Keywords.input as input

# print the number of cans required based on the are and coverage

def paintCalculation():

    height = input.inputInteger()
    weight = input.inputInteger()
    coverage = 7

    cans = (height * weight)/7

    cans = cans.__round__()

    print(cans)

paintCalculation()

