class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

    def __str__(self):
        cur = self
        result = []
        while cur:
            result.append(str(cur.get_val()))
            cur = cur.get_nxt()
        return ' -> '.join(result)

    def get_val(self):
        return self.val

    def get_nxt(self):
        return self.nxt

    def set_val(self, val):
        self.val = val

    def set_nxt(self, nxt):
        self.nxt = nxt


def remove(node, k):
    prev = cur = node
    for _ in range(k - 1):
        prev = cur
        cur = cur.get_nxt()
    prev.set_nxt(cur.get_nxt())


node = cur = Node(1)
for i in range(2, 11):
    cur.set_nxt(Node(i))
    cur = cur.get_nxt()
print(f'node:\n{node}')
remove(node, 5)
print(f'after remove(node, 5):\n{node}')
