import Input_Keywords.input as input

# Check if characters in a string can be rearranged to form a palindrome
# For a string to be rearranged into a palindrome:
#
# At most one character can have an odd frequency.
# All others must have even frequencies.

def canBePalindrome():

    s = input.inputString()
    sum = 0
    count = 0

    if(len(s) %2 == 0):
        for char in s :
            sum ^= ord(char)
            if(sum == 0):
                print(f"{s} can be a palindrome")
                count = 1
                break
    else :
        for char in s:
            sum ^= ord(char)
            if chr(sum) in s:
                print(f"{s} can be a palindrome")
                count = 1
                break
    if count == 0:
        print(f"{s} can't be a palindrome")

canBePalindrome()