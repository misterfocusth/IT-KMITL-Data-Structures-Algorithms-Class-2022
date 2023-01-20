def is_multiple(n, m):
    return n % m == 0


def main():
    n, m = int(input()), int(input())
    print(is_multiple(n, m))


main()
