class OutOfBoundsException(Exception):
    def __init__(self, message="Index out of bounds"):
        self.message = message
        super().__init__(self.message)

class LinkedListNode(object):
    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    @property
    def value(self):
        return self._value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node

    def hasNext(self):
        return self._next is not None

class LinkedList(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0

    def __len__(self):
        return self._len

    @property
    def head(self):
        if self._head:
            return self._head.value
        else:
            return None

    @property
    def tail(self):
        if self._tail:
            return self._tail.value
        else:
            return None

    def append(self, value):
        new_node = LinkedListNode(value)
        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._len += 1

    def insert(self, value):
        new_node = LinkedListNode(value, self._head)
        self._head = new_node
        if not self._tail:
            self._tail = new_node
        self._len += 1

    def removeFirst(self):
        if not self._head:
            raise OutOfBoundsException("List is empty")
        value = self._head.value
        self._head = self._head.next
        if not self._head:
            self._tail = None
        self._len -= 1
        return value

    def getValueAt(self, index):
        if index < 0 or index >= self._len:
            raise OutOfBoundsException("Index out of bounds")
        current = self._head
        for _ in range(index):
            current = current.next
        return current.value

    def toList(self):
        result = []
        current = self._head
        while current:
            result.append(current.value)
            current = current.next
        return result

if __name__ == "__main__":
    ll = LinkedList()
    assert(ll.head is None)
    assert(ll.tail is None)
    assert(ll.toList() == [])
    ll.append(1)
    assert(ll.head == 1)
    assert(ll.tail == 1)
    assert(len(ll) == 1)
    assert(ll.toList() == [1])
    ll.append(2)
    assert(ll.head == 1)
    assert(ll.tail == 2)
    assert(len(ll) == 2)
    assert(ll.toList() == [1, 2])
    ll.append(3)
    assert(ll.head == 1)
    assert(ll.tail == 3)
    assert(len(ll) == 3)
    assert(ll.toList() == [1, 2, 3])
    ll.insert(0)
    assert(ll.head == 0)
    assert(ll.tail == 3)
    assert(len(ll) == 4)
    assert(ll.toList() == [0, 1, 2, 3])
    ll.insert(-1)
    assert(ll.toList() == [-1, 0, 1, 2, 3])
    v = ll.removeFirst()
    assert(v == -1)
    assert(ll.toList() == [0, 1, 2, 3])
    v = ll.removeFirst()
    assert(v == 0)
    assert(ll.toList() == [1, 2, 3])
    v = ll.removeFirst()
    assert(v == 1)
    assert(ll.toList() == [2, 3])
    v = ll.removeFirst()
    assert(v == 2)
    assert(ll.toList() == [3])
    v = ll.removeFirst()
    assert(v == 3)
    assert(ll.toList() == [])
    assert(len(ll) == 0)

    # Testes para a classe OutOfBoundsException
    try:
        ll.getValueAt(0)
    except OutOfBoundsException:
        pass
    else:
        raise AssertionError("OutOfBoundsException not raised for getValueAt(0)")

    try:
        ll.getValueAt(5)
    except OutOfBoundsException:
        pass
    else:
        raise AssertionError("OutOfBoundsException not raised for getValueAt(5)")

    print("100%")
