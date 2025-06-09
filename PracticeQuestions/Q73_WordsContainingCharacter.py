import Input_Keywords.input as input

# 2942. Find Words Containing Character
# You are given a 0-indexed array of strings words and a character x.
#
# Return an array of indices representing the words that contain the character x.

def wordsContainingCharacter():

    list = input.inputListOfString()
    target = input.inputString()
    list2 = []

    for i in range(len(list)):
        word = list[i]
        for char in word:
            if char == target:
                list2.append(i)

    print(list2)
wordsContainingCharacter()