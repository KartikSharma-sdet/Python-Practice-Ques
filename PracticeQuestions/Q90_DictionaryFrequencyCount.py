import Input_Keywords.input as input

# Count the frequency of each character within a string by using dictionary
# Enter any string : aabbaabccccdcdddddeeeeeefeefffffff
# {'a': 4, 'b': 3, 'c': 5, 'd': 6, 'e': 8, 'f': 8}


def DictFrequencyCount():

    s = input.inputString()

    set = {}

    for char in s:
        if set.__contains__(char):
            set[char] += 1
        else:
            set[char] = 1
    print(set)

DictFrequencyCount()