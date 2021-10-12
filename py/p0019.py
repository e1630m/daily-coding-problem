def tract(m):
    lk = len(m[0])
    cost = [0 for _ in range(lk)]
    for r in m:
        cost = [c + min(k for j, k in enumerate(cost) if i != j) for i, c in enumerate(r)]
    return min(cost)


print('matrix = [', end='')
for line in (matrix := [[r * c for c in range(1, 11)] for r in range(1, 11)]):
    print(f'\n\t{line}', end='')
print('\n]')
print('tract(matrix): ', end='')
print(tract(matrix))
