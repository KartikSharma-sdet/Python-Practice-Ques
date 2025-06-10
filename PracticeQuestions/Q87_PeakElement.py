import Input_Keywords.input as input

# Peak Element
# Problem: Find an element in an array which is greater than its neighbors.
# Input: [1, 3, 20, 4, 1, 0] → Output: 20 (or any valid peak)

def peakElement():

    list = input.inputList()
    prev = 0
    curr = 0
    next = 0
    count = 0

    for i in range(1, len(list)-1):

        prev = list[i-1]
        curr = list[i]
        next = list[i+1]

        if prev<=curr and next<=curr:
            print(f"{curr} is a peak element")
            count += 1

    if count == 0:
        print("No peak elements found")

peakElement()


