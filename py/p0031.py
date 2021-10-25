def steps(source, target):
    s, t = len(source) + 1, len(target) + 1
    m = [[c if not r else r if not c else 0 for c in range(s)]
         for r in range(t)]
    for r in range(1, t):
        for c in range(1, s):
            if source[c - 1] == target[r - 1]:
                m[r][c] = m[r - 1][c - 1]
            else:
                m[r][c] = min(m[r - 1][c], m[r][c - 1], m[r - 1][c - 1]) + 1
    return m[-1][-1]


s, t, e = 'kitten', 'sitting', 3
print(f'steps("{s}", "{t}"): {steps(s, t)}, expected: {e}')
