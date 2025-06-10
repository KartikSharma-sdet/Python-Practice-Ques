import Input_Keywords.input as input

# Uncommon Words from Two Sentences
# LeetCode : 884

def UncommonWords():

    s1 = input.inputSentence()
    s1_list = s1.split(" ")
    s2 = input.inputSentence()
    s2_list = s2.split(" ")

    dict1 = {}

    for word1 in s1_list:
        if word1 in dict1:
            dict1[word1] += 1
        else:
            dict1[word1] = 1

    for word2 in s2_list:
        if word2 in dict1:
            dict1[word2] += 1
        else:
            dict1[word2] = 1

    for key in dict1.keys():
        if dict1[key] == 1:
            print(f"'{key}'")

UncommonWords()

