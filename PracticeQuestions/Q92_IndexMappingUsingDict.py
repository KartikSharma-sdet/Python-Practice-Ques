import Input_Keywords.input as input

# Index Mapping using dictionary

def indexMappingUsingDictionary():

    s = input.inputString()

    indexMapDict = {}

    for i in range(len(s)):

        char = s[i]
        if char in indexMapDict:
            indexMapDict[char].append(i)
        else :
            indexMapDict[char] = [i]

    print(indexMapDict)

indexMappingUsingDictionary()