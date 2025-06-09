import Input_Keywords.input as input

# 771. Jewels and Stones
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
#
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

def JewelsAndStones():

    jewels,stones = input.inputJewelsAndStones()
    jewelCount = 0

    for char in stones:
        if char in jewels:
            jewelCount += 1

    print(f"The number of Jewels are {jewelCount}")

JewelsAndStones()