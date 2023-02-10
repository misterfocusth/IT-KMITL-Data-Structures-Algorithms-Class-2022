class ArrayStack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size() == 0

    def push(self, input_data):
        self.data.append(input_data)

    def pop(self):
        if (self.size() == 0):
            return print("Underflow: Cannot pop data from an empty list")
        return self.data.pop()

    def stackTop(self):
        last_idx = self.size() - 1
        return self.data[last_idx]

    def printStack(self):
        print(self.data)


def main():
    myStack = ArrayStack()
    myStack.push(10)
    myStack.push(20)
    myStack.push(30)
    myStack.printStack()
    x = myStack.pop()
    print(x)
    myStack.pop()
    myStack.printStack()
    myStack.pop()
    print(myStack.is_empty())
    myStack.pop()


main()
