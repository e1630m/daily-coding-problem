class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def count_unival(node):
    if node is None:
        return 0
    elif node.left == node.right == None:
        return 1
    elif not node.left and node.val == node.right.val:
        return 1 + count_unival(node.right)
    elif not node.right and node.val == node.left.val:
        return 1 + count_unival(node.left)
    left = count_unival(node.left)
    right = count_unival(node.right)
    return left + right + (node.val == node.left.val == node.right.val)


a = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0))) 
print('a:', count_unival(a))

b = Node(1, Node(2, Node(2), Node(2)), Node(2))
print('b:', count_unival(b))
