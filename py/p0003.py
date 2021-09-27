class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f'Node({repr(self.val)}, {repr(self.left)}, {repr(self.right)})'


def deserialize(s: str) -> Node:
    return eval(s)


def serialize(tree: Node) -> str:
    return repr(tree)


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

print(serialize(node))
print(deserialize(serialize(node)))
