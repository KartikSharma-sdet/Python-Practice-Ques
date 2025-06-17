import Input_Keywords.input as input

def passwordValidator():

   print("Enter your password")
   password = input.inputString()\

   upper = 0
   lower = 0
   digit = 1

   if len(password) < 8:
       return False

   for char in password:

       if char == char.upper():
           upper = 1
       elif char == char.lower():
           lower = 1
       elif char.isdigit():
           digit = 1

   if upper == lower == digit == 1:
     return True
   else:
     return False

bool = passwordValidator()

print(bool)

