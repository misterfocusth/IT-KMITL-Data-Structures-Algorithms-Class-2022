from time import time


def is_intersect(a, b, c):
    is_intersect = False
    for y in range(len(a) - 1):
        if ((a[y] in b) and (a[y] in c)):
            is_intersect = True
            break
    return is_intersect


def analyze_algo(a, b, c):
    start_time = time()
    result = is_intersect(a, b, c)
    end_time = time()
    elapsed = end_time - start_time
    print("[Lab 7.2] - Execution Time : %.4f" % (elapsed))
    print(result)


test_case_1 = analyze_algo([50, 20, 80], [40, 30, 20], [20, 70, 90])
test_case_2 = analyze_algo(
    [40, 60, 80, 100], [10, 30, 50, 60], [10, 20, 30, 40])
