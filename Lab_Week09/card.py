def insertionSort(list, last):
    comparisons = 0
    for i in range(1, last + 1):
        current = list[i]
        j = i - 1
        while j >= 0 and list[j] > current:
            list[j + 1] = list[j]
            j -= 1
            comparisons += 1
        list[j + 1] = current
        print(list)
    if comparisons == 0:
        comparisons = last
    else:
        comparisons = comparisons + last - 1
    print("Comparison times:", comparisons)


def selectionSort(list, last):
    comparisons = 0
    for i in range(last):
        minIndex = i
        for j in range(i + 1, last + 1):
            if list[j] < list[minIndex]:
                minIndex = j
            comparisons += 1
        list[i], list[minIndex] = list[minIndex], list[i]
        print(list)
    print("Comparison times:", comparisons)


def bubbleSort(list, last):
    comparisons = 0
    for i in range(last):
        for j in range(last - i):
            if j != last and list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
            comparisons += 1
        print(list)
    print("Comparison times:", comparisons)


def insertionCardSort(cards, last):
    comparisons = 0
    for i in range(1, last + 1):
        current = cards[i]
        j = i - 1
        while j >= 0 and cardValue(cards[j]) > cardValue(current):
            comparisons += 1
            cards[j + 1] = cards[j]
            j -= 1
        cards[j + 1] = current
        print(cards)
    if comparisons == 0:
        comparisons = last
    else:
        comparisons = comparisons + last - 1
    print("Comparison times:", comparisons)


def selectionCardSort(cards, last):
    comparisons = 0
    for i in range(last):
        min_index = i
        for j in range(i+1, last+1):
            comparisons += 1
            if cardValue(cards[j]) < cardValue(cards[min_index]):
                min_index = j
        cards[i], cards[min_index] = cards[min_index], cards[i]
        print(cards)
    print("Comparison times:", comparisons)


def bubbleCardSort(cards, last):
    comparisons = 0
    for i in range(last):
        for j in range(last-i):
            comparisons += 1
            if cardValue(cards[j]) > cardValue(cards[j+1]):
                cards[j], cards[j+1] = cards[j+1], cards[j]
        if comparisons == 0:
            break
        print(cards)
    print("Comparison times:", comparisons)


def cardValue(card):
    faceValues = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6,
                  "8": 7, "9": 8, "10": 9, "J": 10, "Q": 11, "K": 12, "A": 13}
    suitValues = {"♣": 0, "♦": 1, "♥": 2, "♠": 3}
    return (faceValues[card[:-1]], suitValues[card[-1]])


def main():
    bubbleCardSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)


main()
