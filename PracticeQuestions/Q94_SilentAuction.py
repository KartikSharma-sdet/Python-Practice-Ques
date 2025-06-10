import Input_Keywords.input as input

# Input :
# Enter a name : M
# Enter a bid : 35000
# Do you want to continue ?
# Enter 'yes' or 'no' : yes
# Enter a name : R
# Enter a bid : 50000
# Do you want to continue ?
# Enter 'yes' or 'no' : no

# Output :
# The winner is R with a bid of 50000

def silentAuction():

    dict1 = {}
    check = "yes"
    max = 0
    nameMax = ""

    while(check == "yes"):

        name = input.inputName()
        bid  = input.inputBid()

        if bid > max:
            max = bid
            nameMax = name


        dict1[name] = bid

        print("Do you want to continue ? ")
        check = input.inputYesOrNo()

    print(f"The winner is {nameMax} with a bid of {max}")

silentAuction()






