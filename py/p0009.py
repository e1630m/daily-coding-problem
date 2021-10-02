def nasum(l):
    ll = len(l)
    if ll < 3:
        return max(l) if ll == 2 else l[0] if l else 0
    a = [l[0], max(l[0], l[1])]
    for i, n in enumerate(l[2:]):
        a.append(max(n + a[i], a[-1]))
    return a[-1]


l = [2, 4, 6, 2, 5]
e = 13
print(f'fl: {l} nasum(): {nasum(l)}, expected: {e}')

l = [5, 1, 1, 5]
e = 10
print(f'fl: {l} nasum(): {nasum(l)}, expected: {e}')
