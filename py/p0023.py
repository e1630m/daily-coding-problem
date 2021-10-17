def min_steps(b, start, end):
    h, w = len(b), len(b[0])
    m = [[h * w + 1 if i else 0 for i in r] for r in b]
    m[start[0]][start[1]] = 1
    queue = [start]
    while queue:
        r, c = queue.pop(0)
        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + i, c + j
            if 0 <= nr < h and 0 <= nc < w:
                if not m[nr][nc]:
                    m[nr][nc] = m[r][c] + 1
                    queue.append((nr, nc))
    return m[end[0]][end[1]] - 1 if m[end[0]][end[1]] else None


board = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
s, e = (3, 0), (0, 0)
print('\nboard = [', end='')
for line in board:
    print(f'\n\t{line},', end='')
print('\n]')
print(f'min_steps(board, {s}, {e}): {min_steps(board, s, e)}')

board = [
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
]
s, e = (4, 0), (0, 0)
print('\nboard = [', end='')
for line in board:
    print(f'\n\t{line},', end='')
print('\n]')
print(f'min_steps(board, {s}, {e}): {min_steps(board, s, e)}')

board = [
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
]
s, e = (4, 0), (0, 0)
print('\nboard = [', end='')
for line in board:
    print(f'\n\t{line},', end='')
print('\n]')
print(f'min_steps(board, {s}, {e}): {min_steps(board, s, e)}')

board = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
]
s, e = (5, 0), (0, 0)
print('\nboard = [', end='')
for line in board:
    print(f'\n\t{line},', end='')
print('\n]')
print(f'min_steps(board, {s}, {e}): {min_steps(board, s, e)}')
