from insertion_sort import *
from selection_sort import *
from bubble_sort import *


class test:
    def insertion():
        print("\n===== Insertion Sort =====\n")
        insertion_sort([23, 78, 45, 8, 32, 56], 5)
        insertion_sort([2, 1, 3, 4, 5, 6], 5)
        insertion_sort([503, 87, 512, 61, 908, 170, 897,
                       275, 653, 426, 154, 765, 703], 12)

    def selection():
        print("\n===== Selection Sort =====\n")
        selection_sort([23, 78, 45, 8, 32, 56], 5)
        selection_sort([2, 1, 3, 4, 5, 6], 5)
        selection_sort([503, 87, 512, 61, 908, 170, 897,
                       275, 653, 426, 154, 765, 703], 12)

    def bubble():
        print("\n===== Bubble Sort =====\n")
        bubble_sort([23, 78, 45, 8, 32, 56], 5)
        bubble_sort([2, 1, 3, 4, 5, 6], 5)
        bubble_sort([503, 87, 512, 61, 908, 170, 897,
                     275, 653, 426, 154, 765, 703], 12)


def main():
    test.insertion()
    test.selection()
    test.bubble()


main()
