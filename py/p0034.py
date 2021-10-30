from time import perf_counter_ns as ns


def npal(s):
    if s == s[::-1]:
        return s
    if s[0] == s[-1]:
        return s[0] + npal(s[1:-1]) + s[-1]
    if len(f := s[0] + npal(s[1:]) + s[0]) > len(b := s[-1] + npal(s[:-1]) + s[-1]):
        return b
    elif len(f) < len(b):
        return f
    return min(f, b)


def mpal(s, memo={}):
    if s in memo:
        return memo[s]
    if s == s[::-1]:
        memo[s] = s
        return memo[s] 
    if s[0] == s[-1]:
        memo[s] = s[0] + mpal(s[1:-1]) + s[-1]
        return memo[s]
    f = s[0] + mpal(s[1:]) + s[0]
    b = s[-1] + mpal(s[:-1]) + s[-1]
    if len(f) > len(b):
        memo[s] = b
    elif len(f) < len(b):
        memo[s] = f
    else:
        memo[s] = min(f, b)
    return memo[s]


funcs = (npal, mpal)
tests = ['race', 'google', 'asdkjflldswerpoiuaaaaaa']
for s in tests:
    for func in funcs:
        start = ns()
        result = func(s)
        elapsed = ns() - start
        print(f'{str(func).split()[1]}("{s}"): {result} ({elapsed / 1e3:,.0f}us)')
