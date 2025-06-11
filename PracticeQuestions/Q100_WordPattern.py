import Input_Keywords.input as input

# Q. Given a pattern and a string, check if the pattern matches the string with a one-to-one correspondence.
# Input
# Word string
# Enter any string : cat dog dog cat
# Pattern string
# Enter any string : a b b a
# Output
# {'a': 'cat', 'b': 'dog'}
# True

def word_pattern():

    print("Word string")
    s = input.inputString()
    print("Pattern string")
    pattern = input.inputString()

    listp = pattern.split(" ")
    listw = s.split(" ")
    count = 1

    map = {}
    usedWords = {}

    lengthp = len(listp)
    lengthw = len(listw)

    if(lengthw != lengthp):
        count = 0

    if count == 1:
        for i in range(lengthp):
            p = listp[i]
            w = listw[i]

            if p in map:

                if map[p] != w:
                    count = 0
                    break

            else :
                if w in usedWords:
                    count = 0
                    break
                map[p] = w
                usedWords[w] = True

    print(map)
    if count == 0:
        print("False")
    else :
        print("True")


word_pattern()

