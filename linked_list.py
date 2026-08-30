#Jenna Lee CSC231-002

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def add(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.size += 1

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def append(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

#
    def pop(self, pos=None):
        if self.is_empty():
            raise IndexError("Pop from empty list")
        
        if pos is None:
            pos = self.size - 1
        
        if not isinstance(pos, int):
            raise TypeError("Position must be an integer")
        
        if pos < 0 or pos >= self.size:
            raise IndexError("Position out of range")
        
        if pos == 0:
            data = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return data
        
        prev = None
        current = self.head
        for _ in range(pos):
            prev = current
            current = current.next
        
        data = current.data
        prev.next = current.next
        if current == self.tail:
            self.tail = prev
        self.size -= 1
        return data

    def search(self, item):
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def remove(self, item):
        if self.is_empty():
            return
        if self.head.data == item:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return
        prev = None
        current = self.head
        while current and current.data != item:
            prev = current
            current = current.next
        if current:
            prev.next = current.next
            if current == self.tail:
                self.tail = prev
            self.size -= 1

    