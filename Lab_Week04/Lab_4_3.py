import ArrayStack as A


def infixToPostfix(expression):
    operators = ["*", "/", "+", "-"]
    result = ""
    myStack = A.ArrayStack()

    for exp in expression:

        if exp not in operators:
            result += exp
            continue

        if exp in operators:
            if (myStack.is_empty()):
                myStack.push(exp)
            else:
                current_top = myStack.stackTop()
                top_operand_order = operators.index(current_top)
                current_operand_order = operators.index(exp)

                if current_operand_order > top_operand_order:
                    while not myStack.is_empty():
                        current_top = myStack.pop()
                        result += current_top
                    myStack.push(exp)
                else:
                    myStack.push(exp)

    while not myStack.is_empty():
        current_top = myStack.pop()
        result += current_top

    return result


def main():
    exp = "A+B*C-D/E"
    postfix = infixToPostfix(exp)
    print("Postfix of", exp, "is", postfix)


main()
