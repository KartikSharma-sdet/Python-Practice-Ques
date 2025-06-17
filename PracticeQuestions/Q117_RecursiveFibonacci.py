import Input_Keywords.input as input

def recursiveFibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2)

n = input.inputInteger()
result = recursiveFibonacci(n)
print(result)