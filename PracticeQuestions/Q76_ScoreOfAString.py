import Input_Keywords.input as input

# 3110. Score of a String
# You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
#
# Return the score of string

def scoreOfAString():

    s = input.inputString()
    sum = 0

    for i in range(len(s)-1):
        temp = abs(ord(s[i]) - ord(s[i+1]))
        sum += temp

    print(sum)

scoreOfAString()