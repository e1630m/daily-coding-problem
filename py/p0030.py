def get_max(w, n):
    cur, max_wall = 0, [0] * n
    for i, h in enumerate(w):
        cur = h if h > cur else cur
        max_wall[i] = cur
    return max_wall 


def capa(w):
    n = len(w)
    lmax, rmax = get_max(w, n), get_max(w[::-1], n) 
    return sum(min(lmax[i], rmax[i]) - w[i] for i in range(n))


wall, expected = [3, 0, 1, 3, 0, 5], 8
print(f'capa({wall}): {capa(wall)}, expected: {expected}')
