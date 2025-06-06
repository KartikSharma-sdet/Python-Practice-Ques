import Input_Keywords.input as input

def leap_year():
    year = input.inputInteger()

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"The year {year} is a leap year.")
            else:
                print(f"The year {year} is not a leap year.")
        else:
            print(f"The year {year} is a leap year.")
    else:
        print(f"The year {year} is not a leap year.")

leap_year()







# 1. Attended a status-update session for python at 5:00 pm
# 2. Automated two small tests using record and replay tool of TestComplete:
#   a. To interact with the devices listed within the PCE as they were inaccessible through properties
#   b. To launch two batch files together and interact with them simultaneously
# 3. Currently writing a test script in python using TestComplete for the PCE application
# 4. Solved 5 DSA questions for gaining a better understanding of python and logic.