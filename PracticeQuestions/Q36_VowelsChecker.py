import Input_Keywords.input as input

# vowels checker

def vowels_checker():

    string = input.inputString()
    count = 0

    for char in string:
        if(char == 'a' or char == 'e' or char == 'i' or char == 'u' or char == 'o'):
            count += 1

    print(f"The number of vowels within the string {string} are {count}.")

vowels_checker()