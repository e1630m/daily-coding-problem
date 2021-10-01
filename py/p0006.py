import ctypes


class LinkedList:
    def __init__(self, head):
        self.head = self.tail = head
        self.elements = [head]
        self.id = 0

    def add(self, element):
        self.tail.id ^= id(element)
        element.id = id(self.tail)
        self.tail = element
        self.elements.append(element)

    def get(self, index):
        prv, element = 0, self.head
        for _ in range(index):
            if nxt := prv ^ element.id:
                prv = id(element)
                element = ctypes.cast(nxt, ctypes.py_object).value
            else:
                print('Out of range')
                return None
        return element


class Node:
    def __init__(self, value=None):
        self.value = value
        self.id = 0

    def __repr__(self):
        return str(self.value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_id(self):
        return self.id    


mon, tue, wed, thu, fri = 'Mon Tue Wed Thu Fri'.split()
nmon, ntue, nwed, nthu, nfri = Node(mon), Node(tue), Node(wed), Node(thu), Node(fri)
print(f'mon: {mon}, id(mon): {id(mon)}\n'
      f'tue: {tue}, id(tue): {id(tue)}\n'
      f'wed: {wed}, id(wed): {id(wed)}\n'
      f'nmon: {nmon}, id(nmon): {id(nmon)}\n'
      f'ntue: {ntue}, id(ntue): {id(ntue)}\n'
      f'nwed: {nwed}, id(nwed): {id(nwed)}\n'
      f'nmon.get_value(): {nmon.get_value()}\n'
      f'ntue.get_value(): {ntue.get_value()}\n'
      f'nwed.get_value(): {nwed.get_value()}\n'
      f'nmon.get_value() is mon: {nmon.get_value() is mon}\n'
      f'ntue.get_value() is tue: {ntue.get_value() is tue}\n'
      f'nwed.get_value() is wed: {nwed.get_value() is wed}')

ll = LinkedList(nmon)
ll.add(ntue)
ll.add(nthu)
ll.add(nfri)
ll.add(nwed)

print(f'll = LinkedList(nmon), after ll.add(ntue), ll.add(nthu), ll.add(nfri), ll.add(nwed)\n'
      f'll.head: {ll.head}, ll.tail: {ll.tail}, ll.tail.id: {ll.tail.id}, ll.elements: {ll.elements}\n'
      f'll.get(0): {ll.get(0)}, ll.get(1): {ll.get(1)}, ll.get(2): {ll.get(2)}, ll.get(3): {ll.get(3)}, ll.get(4): {ll.get(4)}')
