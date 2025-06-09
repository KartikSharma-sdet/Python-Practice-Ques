import Input_Keywords.input as input

# Find the word which contains maximum vowels from a given sentence

def maxVowelsInASentence():

    s = input.inputString()
    words = s.split(" ")
    vowels = "aeiouAEIOU"
    count = 0
    result = ""

    for word in words:
        count = 0
        for char in word:
            if vowels.__contains__(char):
                count += 1

        if count > len(result):
            result = word

    print(result)
maxVowelsInASentence()