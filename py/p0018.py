def naive(arr, k):  # O(kn)
    return [max(arr[i:i + k]) for i in range(len(arr) - k + 1)]


def on(a, k):
    order = [0]
    for i in range(1, k):
        while a[i] >= a[order[-1]]:
            order.pop()
        order.append(i)
    for i in range(k, len(a)):
        print(f'{a[order[0]]} ', end='')
        while order and order[0] <= i - k:
            order.pop(0)
        while order and a[i] >= a[order[-1]]:
            order.pop()
        order.append(i)
    print(a[order[0]])


a, k, e = [10, 5, 2, 7, 8, 7], 3, [10, 7, 8, 8]
print(f'naive({a}, {k}): {naive(a, k)}, expected: {e}')
print(f'on({a}, {k}): ', end='')
on(a,k)
