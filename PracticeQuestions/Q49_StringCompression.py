import Input_Keywords.input as input

# input : aabbcccdddd
# output : a2b2c3d4

def stringCompression():

    string = input.inputString()
    s = ""
    count = 1

    if len(string) <= 1:
        print(string)
    else:

        for i in range(1 ,len(string)):

            if string[i] == string[i-1]:
                count+=1
            else:
                s += string[i - 1]
                if (count > 1):
                    s += str(count)
                count = 1

            if string[i] == string[i - 1] and i == len(string)-1:
                s += string[i - 1]
                if (count > 1):
                    s += str(count)


        print(s)

stringCompression()



