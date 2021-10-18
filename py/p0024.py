class BinaryTree:
    def __init__(self, val, lft=None, rgt=None, parent=None):
        self.val = val
        self.lft = lft
        self.rgt = rgt
        self.parent = parent
        self.locked = False
        self.locked_desc = 0

    def is_locked(self):
        return self.locked

    def is_modifiable(self):
        if self.locked_desc:
            return False
        current = self.parent
        while current:
            if current.locked:
                return False
            current = current.parent
        return True

    def lock(self):
        if self.locked or not self.is_modifiable():
            return False
        self.locked = True
        current = self.parent
        while current:
            current.locked_desc += 1
            current = current.parent
        return True

    def unlock(self):
        if not self.locked or not self.is_modifiable():
            return False
        self.locked = False
        current = self.parent
        while current:
            current.locked_desc -= 1
            current = current.parent
        return True


current = bt = BinaryTree(1)
for i in range(2, 8):
    lft, rgt = BinaryTree(i), BinaryTree(i)
    current.lft, current.rgt = lft, rgt
    lft.parent, rgt.parent = current, current
    current = lft

print(f'bt.lft.lft.lft.val: {bt.lft.lft.lft.val}')
print(f'bt.lft.lft.lft.is_locked(): {bt.lft.lft.lft.is_locked()}')
print(f'bt.lft.lft.lft.lft.lock(): {bt.lft.lft.lft.lft.lock()}')
print(f'bt.lft.lft.lft.locked_desc: {bt.lft.lft.lft.locked_desc}')
print(f'bt.lft.lft.lft.is_locked(): {bt.lft.lft.lft.is_locked()}')
print(f'bt.lft.lft.lft.lock(): {bt.lft.lft.lft.lock()}')