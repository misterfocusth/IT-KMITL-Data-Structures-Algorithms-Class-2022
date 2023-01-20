import json


def minmax(data):
    min, max = 0, 0
    for x in range(0, len(data) - 1, 1):
        if x == 0:
            min, max = data[x], data[x]
        if data[x] <= min:
            min = data[x]
        if data[x] >= max:
            max = data[x]
    return min, max


def main():
    print(minmax(json.loads(input())))


main()
