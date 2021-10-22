def is_bracket_valid(b):
    if not b:
        return True
    if any(b.count(p[0]) != b.count(p[1]) for p in '() {} []'.split()):
        return False
    removed = b.replace('()', '').replace('{}', '').replace('[]', '')
    if len(b) == len(removed):
        return False
    return is_bracket_valid(removed)

p = '([])[]({})'
print(f'is_braket_valid("{p}"): {is_bracket_valid(p)}')
p = '([)]'
print(f'is_braket_valid("{p}"): {is_bracket_valid(p)}')
p = '((()'
print(f'is_braket_valid("{p}"): {is_bracket_valid(p)}')
