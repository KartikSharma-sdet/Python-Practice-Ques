import Input_Keywords.input as input

#Nested If – Grade Calculator
#Ask the user to enter a score (0–100). Using nested if, classify:
#90–100: A
#80–89: B
#70–79: C
#60–69: D
#<60: F

def gradeCalculator():

    marks = input.inputInteger()

    if(marks >100 or marks<0):
        print("Please enter a number within 0 and 100")
    elif(marks >= 90 and marks <= 100 ):
        print("Grade : B")
    elif (marks >= 80 and marks <= 89):
        print("Grade : C")
    elif (marks >= 70 and marks <= 79):
        print("Grade : D")
    elif (marks >= 60 and marks <= 69):
        print("Grade : A")
    elif (marks < 60):
        print("Grade : F")
gradeCalculator()