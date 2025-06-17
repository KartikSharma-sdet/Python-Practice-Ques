import Input_Keywords.input as input

def towerOfHanoi(n, src ,helper, destination):

    if n == 1:
        print(f"transfer disk {n} from {src} to {destination}")
        return
    towerOfHanoi(n-1, src, destination, helper)
    print(f"transfer disk {n-1} from {src} to {destination}")
    towerOfHanoi(n-1, helper, src, destination)



print("Input the number of disks")
n = input.inputInteger()
towerOfHanoi(n, "S", "H", "D")