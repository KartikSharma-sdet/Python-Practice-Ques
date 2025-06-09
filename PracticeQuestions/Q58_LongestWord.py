import Input_Keywords.input as input

# input = I am a boy
# output = boy

def longestWord():

    string = input.inputString()
    string += " "
    word = ""
    max = 0
    tempWord = ""

    for char in string:

        if char == " ":
            temp = len(word)
            if temp > max:
                max = temp
                tempWord = word
            word = ""
        else:
            word += char

    print(f"{tempWord} is the longest word in '{string}' with {max} characters")

longestWord()