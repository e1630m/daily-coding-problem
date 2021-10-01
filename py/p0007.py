def count_possible_dec(s):
    if s.startswith('0'):
        return 0
    if len(s) < 2:
        return 1
    count = 0
    count += count_possible_dec(s[2:]) if int(s[:2]) < 27 else 0
    count += count_possible_dec(s[1:])
    return count


print(count_possible_dec('1111'))  # 5 (aaaa, kaa, aka, aak, kk)
