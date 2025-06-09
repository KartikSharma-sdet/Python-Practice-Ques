import Input_Keywords.input as input

# Write 2 programs for converting celsius to fahrenheit and vice versa

def CelsiusToFahrenheit():
    celsius = input.inputFloat()

    fahrenheit = (celsius * 9 / 5) + 32

    print(f"{celsius} in fahrenheit is {fahrenheit}")

def FahrenheitToCelsius():
    fahrenheit = input.inputFloat()

    celsius = (fahrenheit - 32) * 5 / 9

    print(f"{fahrenheit} in celsius is {celsius}")

CelsiusToFahrenheit()
FahrenheitToCelsius()