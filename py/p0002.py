from time import perf_counter_ns as ns


def prod(arr):
    p = 1
    for n in arr:
        p *= n
    return p


def brute(arr):
    ans = [prod([n for i, n in enumerate(arr) if i != j]) for j in range(len(arr))]
    return ans


def div(arr):  # doesn't work on large arr
    return [prod(arr) / n for n in arr]


def no_div(arr, ans=[]):
    p = 1
    for n in arr[::-1]:
        ans.insert(0, p)
        p *= n
    p = 1
    for i, n in enumerate(arr):
        ans[i] *= p
        p *= n
    return ans


tests = [
    [1, 2, 3, 4, 5],
    [3, 2, 1],
]

f = {'brute': [], 'div': [], 'no_div': []}
for n in tests:
    start = ns()
    brute(n)
    end = ns()
    f['brute'].append(end - start)
    start = ns()
    div(n)
    end = ns()
    f['div'].append(end - start)
    start = ns()
    no_div(n)
    end = ns()
    f['no_div'].append(end - start)
print(f'brute(): {f["brute"]}, div(): {f["div"]}, no_div(): {f["no_div"]}')
