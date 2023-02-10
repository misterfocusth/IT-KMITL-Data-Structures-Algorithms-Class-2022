class ArrayStack:

    def __init__(self) -> None:
        self.data = []

    def size(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):
        self.data.append(e)

    def pop(self):
        if self.is_empty():
            print("Underflow: Cannot pop data from an empty list")
        else:
            return self.data.pop()

    def stackTop(self):
        if self.is_empty():
            return None
        else:
            return self.data[-1]

    def printStack(self):
        print(self.data)
