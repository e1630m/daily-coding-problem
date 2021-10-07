def longest_substring(s, k):
    if not k:
        return 0
    longest = current = s[0]
    for i, c in enumerate(s[1:]):
        current += c
        if len(set(current)) > k:
            longest, current = current[:-1], [c]
    return len(longest)


s, k = "abcba", 2
print(f'longest_substring("{s}", {k}): {longest_substring(s, k)}')
s, k = "abccdccdde", 2
print(f'longest_substring("{s}", {k}): {longest_substring(s, k)}')
s, k = "abcddefghhi", 4
print(f'longest_substring("{s}", {k}): {longest_substring(s, k)}')
