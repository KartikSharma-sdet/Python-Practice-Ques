import Input_Keywords.input as input

# Isomorphic Strings
# Check if characters in one string can be replaced to get the second string.

def isomorphicStrings():

    print("String 1")
    s1 = input.inputString()
    print("String 2")
    s2 = input.inputString()

    if len(s1) != len(s2):
        return False

    dict = {}

    for i in range(len(s1)):
        word = s1[i]
        replacement = s2[i]

        if word not in dict.keys():
            if replacement not in dict.values():
                dict[word] = replacement
            else :
                return False
        else:
            if dict[word] != replacement:
                return False

    return True

bool = isomorphicStrings()
print(bool)