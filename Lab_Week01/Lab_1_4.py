def multiply(n):
    result = 0
    for x in range(1, n+1, 1):
        result += x ** 2
    return result


def multiply_odd(n):
    result = 0
    for x in range(1, n+1, 2):
        result += x ** 2
    return result


def main():
    n = int(input())
    print(multiply(n))
    print(multiply_odd(n))


main()
