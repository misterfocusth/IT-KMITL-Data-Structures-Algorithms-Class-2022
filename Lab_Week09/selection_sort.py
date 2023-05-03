def selection_sort(array, size):
    comparison_times = 0
    for step in range(size):
        comparison_times += 1
        min_idx = step
        for i in range(step + 1, size):
            comparison_times += 1
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])
        print(array)
    print("Comparison Times:", comparison_times, "\n")
