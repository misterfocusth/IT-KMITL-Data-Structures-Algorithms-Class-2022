import ArrayStack


def is_parentheses_matching(expression):
    myStack = ArrayStack.ArrayStack()

    for chr in expression:
        if chr in ["(", ")"]:
            if myStack.is_empty():
                myStack.push(chr)
                continue

            if chr == "(" and myStack.stackTop() == ")":
                myStack.pop()
            elif chr == ")" and myStack.stackTop() == "(":
                myStack.pop()
            else:
                myStack.push(chr)

    return print(myStack.is_empty())


is_parentheses_matching("((A-B)*C)")
is_parentheses_matching("(((A-B)*C")
