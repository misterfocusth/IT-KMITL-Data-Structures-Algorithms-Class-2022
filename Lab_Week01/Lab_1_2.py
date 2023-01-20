def is_even(n):
    is_even = True
    for _ in range(n):
        is_even = not is_even
    return is_even


def main():
    print(is_even(int(input())))


main()
