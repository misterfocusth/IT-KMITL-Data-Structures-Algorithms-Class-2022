from time import time
import random


def randomList(n):
    result = []
    for _ in range(n):
        new_num = random.randint(0, 9999999)
        if (new_num in result):
            continue
        else:
            result.append(new_num)
    return result


def is_intersect_1(a, b, c):
    is_intersect = False
    for x in range(len(a) - 1):
        if (a[x] in b and a[x] in c):
            is_intersect = True
            break
    return is_intersect


def is_intersect_2(a, b, c):
    is_intersect = False
    for x in range(len(a) - 1):
        for _ in range(len(a) - 1):
            for _ in range(len(a) - 1):
                if (a[x] in b and a[x] in c):
                    is_intersect = True
                    break
    return is_intersect


def analyze_algo(n, flag):
    a, b, c = randomList(n), randomList(n), randomList(n)
    start_time = time()
    result = is_intersect_1(a, b, c) if flag == 0 else is_intersect_2(a, b, c)
    end_time = time()
    elapsed = end_time - start_time
    print("[Lab 7.2] - Execution Time [Flag : %s] [N = %s] [Result: %s] : %.4f" %
          (str(flag), str(n), result, elapsed))


analyze_algo(100, 0)
analyze_algo(1000, 0)

analyze_algo(100, 1)
analyze_algo(1000, 1)

analyze_algo(10000, 0)
analyze_algo(100000, 0)

analyze_algo(10000, 1)
analyze_algo(100000, 1)
