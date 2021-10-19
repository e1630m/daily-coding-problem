def match(r, s):
    if all(c not in r for c in '.*'):
        return r == s
    f = len(s) > 0 and r[0] in '.' + s[0]
    if len(r) >= 2 and r[1] == '*':
        return match(r[2:], s) or f and match(r, s[1:])
    return f and match(r[1:], s[1:])


tests = [
    ['ra.', 'ray', True],
    ['ra.', 'raymond', False],
    ['.*at', 'chat', True],
    ['.*at', 'chats', False]
]
for reg, string, expected in tests:
    print(f'match("{reg}", "{string}"): {match(reg, string)}, '
          f'expected: {expected}')
