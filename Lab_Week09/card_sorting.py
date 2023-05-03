class card_sorting():
    def insertion_sort():
        comparison_times = 0
        if len(list) <= 1:
            return
        for current_idx in range(1, len(list)):
            comparison_times += 1
            hold_key = list[current_idx]
            walker = current_idx - 1
            while (walker >= 0 and hold_key < list[walker]):
                comparison_times += 1
                list[walker + 1] = list[walker]
                walker -= 1
            list[walker + 1] = hold_key
            print(list)
        print("Comparison Times:", comparison_times, "\n")
