from time import perf_counter_ns


def ifib(n, x={1, 2}):  # only works for the default x = {1, 2}
    a = b = 1
    for _ in range(1, n):
        a, b = b, a + b
    return b


def rfib(n, x={1, 2}):
    if n <= 0:
        return int(n == 0)
    return sum(rfib(n - step, x) for step in x)


def dp(n, x={1, 2}):
    if n <= min(x):
        return int(n == min(x))
    arr = [0] * (n + 1)
    arr[0] = 1
    for i in range(1, n + 1):
        arr[i] += sum(arr[i - step] for step in x if i >= step)
    return arr[-1]


for name, func in {'ifib': ifib, 'rfib': rfib, 'dp': dp}.items():
    for n, x in ((4, {1, 2}), (10, {1, 2, 3}), (30, {1, 3, 5})):
        start = perf_counter_ns()
        result = func(n, x)
        end = perf_counter_ns()
        print(f'{name}({n}, {x}): {result}, took {end - start:,}ns')
