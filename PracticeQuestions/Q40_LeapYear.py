import Input_Keywords.input as input

# Calculate whether the input year is a leap year or not

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