import Input_Keywords.input as input

# 1108. Defanging an IP Address
# Given a valid (IPv4) IP address, return a defanged version of that IP address.
#
# A defanged IP address replaces every period "." with "[.]".

def defangingIPaddress():

    s = input.inputString()
    prev = ""
    new = ""

    for i in range(len(s)):
        char = s[i]
        if char == '.':
            new += '['
            new += char
            new += ']'
        else:
            new+= char

    print(new)

defangingIPaddress()