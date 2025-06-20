import Input_Keywords.input as input

class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self) -> int:
        if not self.isEmpty():
            temp = self.items.pop()
        return temp

    def pop(self, element) -> int:
        if not self.isEmpty():
            temp = self.items.pop(element)
        return temp

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]

    def isEmpty(self):
        return len(self.items) == 0

stack = Stack()



stack.push("a")
print(stack.peek())