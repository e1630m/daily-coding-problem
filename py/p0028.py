def justify(txt: list, k: int):
    lines, line = [], []
    for word in txt:
        if len(word) + len(line) + sum(len(w) for w in line) <= k:
            line.append(word)
        else:
            lines.append(line)
            line = []
            line.append(word)
    lines.append(line)
    ans = []
    while lines:
        words = lines.pop(0)
        diff = k - len(''.join(words))
        n = len(words) - (len(words) > 1)
        q, r = divmod(diff, n)
        ans.append([w + ' ' * (q * (i < n) + r * (i == 0)) 
                    for i, w in enumerate(words)])
    return [''.join(line) for line in ans]


t, k = 'the quick brown fox jumps over the lazy dog'.split(), 16
print(f'justify({t}, {k}):')
print(justify(t, k))
