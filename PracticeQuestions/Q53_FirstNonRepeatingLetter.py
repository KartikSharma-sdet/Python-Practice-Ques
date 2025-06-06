import Input_Keywords.input as input

def firstNonRepeatingLetter():

    string = input.inputString()

    count = 0
    flag = 0

    for i in string:
        count = 0
        for j in range (0, len(string)):
            if i == string[j]:
                count +=1
        if count == 1 :
            print(f"{i} is the first non repeating letter in {string}")
            flag = 1
            break

    if flag == 0:
        print("Unsuccessful")

firstNonRepeatingLetter()