def find(q, s):
    return [w for w in set(s) if w.startswith(q)]


def rfind(q, s):  
    if q == '':
        return s
    ns = [s[i][1:] for i in range(len(s)) if s[i] and s[i][0] == q[0]]
    return [q[0] + w for w in rfind(q[1:], ns)]


class Node():
    def __init__(self):
        self.children = {}
        self.val = None

    def insert(self, word: str):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.val = word

    def find(self, word: str):
        node = self
        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]
        return self.complete(node, list(word), [])

    def complete(self, root, prefix: list, results):
        if root.val is not None:
            results.append(''.join(prefix))
        for c in root.children:
            prefix.append(c)
            self.complete(root.children[c], prefix, results)
            del prefix[-1]
        return results


query = 'de'
strings = ['dog', 'deer', 'deal']
print(f'find({query}, {strings}): {find(query, strings)}')
print(f'rfind({query}, {strings}): {rfind(query, strings)}')
n = Node()
for w in strings:
    n.insert(w)
print(f'nfind({query}, {strings}): {n.find(query)}')
