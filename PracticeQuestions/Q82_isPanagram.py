import Input_Keywords.input as input

# Check whether a string contains any alphabets or not?
# abcdef10 is not a panagram

def isPanagram():

    s = input.inputString()
    count = 0

    for alpha in s:
        if '0'<=alpha <='9':
            print(f"'{s}' is not a panagram")
            count = 1
            break

    if(count == 0):
        print(f"'{s}' is a panagram")

isPanagram()

