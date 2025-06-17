import Input_Keywords.input as input

def groupByMarks():

    print("Enter length for student's dictionary")
    length = input.inputLength()

    studentsDict = input.inputDictionary(length)

    result = {}

    for key in studentsDict.keys():
        marks = studentsDict[key]
        name = key

        if marks in result:
            result[marks].append(name)
        else:
            result[marks] = [name]

    print(result)

groupByMarks()