from heapq import heappush, heappop


def naive(s):
    ans = ['']
    for i, n in zip(range(1, len(s) + 1), s):
        l = sorted(s[:i])
        m = l[i // 2] if i % 2 else (l[i // 2] + l[i // 2 - 1]) / 2
        ans.append(f'{m if m != int(m) else int(m)}')
    return '\n'.join(ans)


def heap(s):
    min_h, max_h, ans = [], [], ['']
    for n in s:
        heappush(min_h, n)
        if len(min_h) > len(max_h) + 1:
            heappush(max_h, -heappop(min_h))
        m = (min_h[0] - max_h[0]) / 2 if len(min_h) == len(max_h) else min_h[0]
        ans.append(f'{m if m != int(m) else int(m)}')
    return '\n'.join(ans) 


seq = [2, 1, 5, 7, 2, 0, 5]
print(f'naive({seq}): {naive(seq)}')
print(f'heap({seq}): {heap(seq)}')
