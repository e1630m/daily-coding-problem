class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.nxt = next_node

    def get_val(self):
        return self.val

    def get_next(self):
        return self.nxt
    
    def set_next(self, next_node):
        self.nxt = next_node


def node_length(node):
    if node.nxt is None:
        return 0
    return 1 + node_length(node.get_next())


def intxn(a, b):
    if (la := node_length(a)) > (lb := node_length(b)):
        for _ in range(la - lb):
            a = a.get_next()
    else:
        for _ in range(lb - la):
            b = b.get_next()
    while a != b:
        a, b = a.get_next(), b.get_next()
    return a

n1, n3, n7, n8, n99 = Node(1), Node(3), Node(7), Node(8, Node(10)), Node(99)
n7.set_next(n8), n1.set_next(n8), n3.set_next(n7), n99.set_next(n1)
a = n3
b = n99
print(f'a: {a.get_val()}, b: {b.get_val()}')
print(f'a.nxt: {a.get_next().get_val()}, b.nxt: {b.get_next().get_val()}')
print(f'a.nxt.nxt: {a.get_next().get_next().get_val()}, '
      f'b.nxt.nxt: {b.get_next().get_next().get_val()}')
print(f'a.nxt.nxt.nxt: { a.get_next().get_next().get_next().get_val()}, '
      f'b.nxt.nxt.nxt: { a.get_next().get_next().get_next().get_val()}')
print(f'id(a.nxt.nxt): {id(a.get_next().get_next())}, '
      f'id(b.nxt.nxt): {id(b.get_next().get_next())}')
print(f'intxn(a, b): {intxn(a, b).get_val()}, id: {id(intxn(a, b))}')
