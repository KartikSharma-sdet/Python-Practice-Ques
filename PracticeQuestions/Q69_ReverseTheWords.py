import Input_Keywords.input as input

# Reverse the given sentence but not the words

def reverseTheWords():

    s = input.inputString()

    s2 = s.split(" ")
    result = ""

    for i in range(len(s2)-1, -1, -1):
        word = s2[i]
        result += word
        result += " "

    print(result)

reverseTheWords()