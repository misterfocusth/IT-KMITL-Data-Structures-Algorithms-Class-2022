from time import time


def summation(n, flag=0):
    result = 0
    if flag == 0:
        for x in range(1, n):
            result += x
    else:
        result = n * (n+1) / 2
    return result


def analyze_algo(n, flag):
    start_time = time()
    summation(n, flag)
    end_time = time()
    elapsed = end_time - start_time
    print("[Lab 7.1] - Execution Time [Flag : %s] [N = %s] : %.4f" %
          (str(flag), str(n), elapsed))


analyze_algo(100, 0)
analyze_algo(10000, 0)
analyze_algo(1000000, 0)
analyze_algo(100000000, 0)
analyze_algo(1000000000, 0)

print("")

analyze_algo(100, 1)
analyze_algo(10000, 1)
analyze_algo(1000000, 1)
analyze_algo(100000000, 1)
analyze_algo(1000000000, 1)
