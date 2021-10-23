def encoder(s):
    encoded = ''
    count, current = 1, s[0]
    for c in s[1:]:
        if c == current:
            count += 1
        else:
            encoded += str(count) + current
            count = 1
            current = c
    return encoded + str(count) + current

s, e = 'AAAABBBCCDAA', '4A3B2C1D2A'
print(f'encoder("{s}"): {encoder(s)}, expected: {e}')

s, e = 'AAAABBBCCDAABCB', '4A3B2C1D2A1B1C1B'
print(f'encoder("{s}"): {encoder(s)}, expected: {e}')
