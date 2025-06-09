import Input_Keywords.input as input

# 58. Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.

def lengthOfLastWord():

    string = input.inputString()
    count = 0

    for i in range(len(string)-1, -1, -1):
        if string[i] == " ":
            break
        else:
            count += 1

    print(f"{count} is the length of the last word in {string}.")

lengthOfLastWord()