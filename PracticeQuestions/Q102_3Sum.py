import Input_Keywords.input as input

# 3 Sum
# Find all unique triplets in the array that sum up to 0.

def threeSum():

    list = input.inputList()
    target = input.inputInteger()
    set1 = set()

    for i in range(len(list)):
        num1 = list[i]
        left = i+1
        right = len(list)-1

        while left < right:
            num2 = list[left]
            num3 = list[right]

            if target == num1+num2+num3 and num1!=num2!=num3:
                set1.add((num1, num2, num3))

            left += 1
            right -= 1

    print(set1)

threeSum()