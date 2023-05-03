def bubble_sort(list, last=0):
    comparison_times = 0
    size = len(list)
    for current_idx in range(size):
        comparison_times += 1
        for x in range(0, current_idx - size - 1):
            comparison_times += 1
            if list[x] > list[x + 1]:
                list[x], list[x + 1] = list[x + 1], list[x]
        print(list)
    print("Comparison Times:", comparison_times, "\n")
