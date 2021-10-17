def sentence(string, words):
    ans, cur = [], ''
    for c in string:
        cur += c
        if cur in words:
            ans.append(cur)
            cur = ''
    return ans


s = 'thequickbrownfox'
w = 'quick', 'brown', 'the', 'fox'
e = [['the', 'quick', 'brown', 'fox']]
r = sentence(s, w)
print(f'sentence({s}, {w}) -> {r} ({"correct" if r in e else "incorrect"})')

s = 'bedbathandbeyond'
w = 'bed', 'bath', 'bedbath', 'and', 'beyond'
e = [['bed', 'bath', 'and', 'beyond'], ['bedbath', 'and', 'beyond']]
r = sentence(s, w)
print(f'sentence({s}, {w}) -> {r} ({"correct" if r in e else "incorrect"})')
