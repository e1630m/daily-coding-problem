class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def get_val(self):
        return self.val

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right


def second_largest(node):
    def search(n):
        if n is None:
            return
        if (l := n.get_left()):
            val.append(l.get_val())
            search(l)
        if (r := n.get_right()):
            val.append(r.get_val())
            search(r)
    val = []
    search(node)
    return sorted(val)[-2]


node = Node(1, Node(2, Node(3, Node(4), Node(33)), Node(22)), Node(10, right=Node(20, right=Node(30, Node(5), right=Node(40)))))
print('node = Node(1, Node(2, Node(3, Node(4), Node(33)), Node(22)), Node(10, right=Node(20, right=Node(30, Node(5), right=Node(40)))))')
print(f'second_largest(node): {second_largest(node)}')
