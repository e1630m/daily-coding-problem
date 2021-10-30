def rt_arbitrage(rate, verbose=False):
    # roundtrip only
    n = {0: 'USD', 1: 'EUR', 2: 'JPY', 3: 'GBP', 4: 'CNY'}
    routes = []
    for r in range(len(rate)):
        for c in range(len(rate)):
            if r != c:
                if rate[r][c] * rate[c][r] > 1:
                    routes.append(((r, c), (c, r)))
    if verbose:
        print('\n'.join([f'{n[fs]}:{n[fe]} -> {n[ss]}:{n[se]}: {rate[fs][fe] * rate[ss][se]:,.4f}'
                        for (fs, fe), (ss, se) in routes]))
    return True if routes else False


def log(x):
    return 1000.0 * ((x**(1 / 1000.0)) - 1)


def arbitrage(rate):
    g = [[-log(c) if c else c for c in r] for r in rate]
    d = [float('inf')] * (n := len(g))
    d[0] = 0
    for _ in range(n - 1):
        for r in range(n):
            for c in range(n):
                d[c] = d[r] + g[r][c] if d[c] > d[r] + g[r][c] else d[c] 
    for r in range(n):
        for c in range(n):
            if d[c] > d[r] + g[r][c]:
                return True
    return False 


# As of Oct 26, 2021 12:10 UTC+00
#  -  USD EUR JPY GBP CNY
# USD  -
# EUR      -
# JPY          -
# GBP              -
# CNY                  -
table = [
    [     0, 0.8605, 113.9780, 0.7243, 6.3792],
    [1.1617,      0, 132.4190, 0.8415, 7.4100],
    [0.0088, 0.0076,        0, 0.0064, 0.0559],
    [1.3805, 1.1882, 157.3470,      0, 8.8068],
    [0.1568, 0.1349,  17.8390, 0.1135,      0]
]
print('table = [\n\t[' + ']\n\t['.join(','.join(str(n).rjust(10) for n in line) for line in table) + ']]')
print(f'rt_arbitrage(table): {rt_arbitrage(table, verbose=False)}')
print(f'arbitrage(table): {arbitrage(table)}')
