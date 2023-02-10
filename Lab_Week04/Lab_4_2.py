import ArrayStack as A


def copyStack(stack1: A.ArrayStack, stack2: A.ArrayStack):
    temp_stack = A.ArrayStack()

    while not stack1.is_empty():
        current_top = stack1.pop()
        temp_stack.push(current_top)

    while not stack2.is_empty():
        stack2.pop()

    while not temp_stack.is_empty():
        current_top = temp_stack.pop()
        stack1.push(current_top)
        stack2.push(current_top)


def main():
    s1 = A.ArrayStack()
    s1.push(10)
    s1.push(20)
    s1.push(30)

    s2 = A.ArrayStack()
    s2.push(10)

    copyStack(s1, s2)

    s1.printStack()
    s2.printStack()


main()
