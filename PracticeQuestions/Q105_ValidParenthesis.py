import Input_Keywords.input as input

# Check Balanced Parentheses with Stack
# Check if the string of brackets is valid.

def validParenthesis() ->str:

    s = input.inputString()
    stack = []

    for char in s:

        if char == '(' or char == '[' or char == '{':
            stack.append(char)
        else:
            if len(stack) == 0:
                return False,s

            c = stack.pop()
            if c == '(' and char != ')':
                return False,s
            elif c == '[' and char != ']':
                return False,s
            elif c == '{' and char != '}':
                return False,s

    if len(stack) == 0:
        return True,s
    else:
        return False,s

bool,s = validParenthesis()
if bool == True:
    print(f"{bool}, {s} are valid parenthesis")
else :
    print(f"{bool}, {s} are invalid parenthesis")