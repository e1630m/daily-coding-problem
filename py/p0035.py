from time import perf_counter_ns as ns


def swap(a):
    a = [c for c in a]
    r, g, b = 0, 0, len(a) - 1
    while g <= b:
        if a[g] == 'R':
            a[r], a[g] = a[g], a[r]
            r += 1
            g += 1
        elif a[g] == 'G':
            g += 1
        else:
            a[g], a[b] = a[b], a[g]
            b -= 1
    return a


def verifier(a):
    r = ['R'] * a.count('R')
    g = ['G'] * a.count('G')
    b = ['B'] * a.count('B')
    return r + g + b


tests = [
    [['G', 'B', 'R', 'R', 'B', 'R', 'G'], ['R', 'R', 'R', 'G', 'G', 'B', 'B']],
    [['B', 'G', 'G', 'R', 'R', 'R', 'R', 'G'], ['R', 'R', 'R', 'R', 'G', 'G', 'G', 'B']]
]

funcs = [swap, verifier]
for arr, expected in tests:
    for f in funcs:
        fn = str(f).split()[1]
        s = ns()
        r = f(arr)
        e = ns() - s
        print(f'{fn}({arr}): {f(arr)} ({"correct" if r == expected else "incorrect"}) ({e / 1e3:,.0f}us)')
