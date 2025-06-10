import Input_Keywords.input as input

# input : (())()    : true
# input : )()(())   : false

def balancedParanthesis():

    s = input.inputString()
    count = 0

    for char in s :
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1

        if count < 0:
            break

    if count == 0:
        print(f"{s} has balanced Parenthesis")
    else :
        print(f"{s} does not have balanced parenthesis")

balancedParanthesis()