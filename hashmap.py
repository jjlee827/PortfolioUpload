#Jenna Lee CSC 231-001

class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None

class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size
        self.keys = []

    def __setitem__(self, key, value):
        index = hash(key) % self.size
        node = self.table[index]
        if node is None:
            self.table[index] = Node(key, value)
            self.keys.append(key)
            return
        prev = None
        while node is not None:
            if node.key == key:
                node.value = value
                return
            prev = node
            node = node.next
        prev.next = Node(key, value)
        self.keys.append(key)

    def __getitem__(self, key):
        index = hash(key) % self.size
        node = self.table[index]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        raise KeyError
    
    def __delitem__(self, key):
        index = hash(key) % self.size
        node = self.table[index]
        prev = None
        while node is not None:
            if node.key == key:
                if prev is None:
                    self.table[index] = node.next
                else:
                    prev.next = node.next
                self.keys.remove(key)
                return
            prev = node
            node = node.next
        raise KeyError
    
    def __contains__(self, key):
        index = hash(key) % self.size
        node = self.table[index]
        while node is not None:
            if node.key == key:
                return True
            node = node.next
        return False
    
    def get_keys(self):
        return self.keys[:]
    

if __name__ == "__main__":
    hm = HashMap()

    print("\n--Test 1--")
    hm["apple"] = 10
    hm["banana"] = 20
    hm["orange"] = 30
    print("Should be 10: ", hm["apple"])
    print("Should be 20: ", hm["banana"])
    print("Shoudl be 30: ", hm["orange"])

    print("\n--Test 2--")
    hm["apple"] = 99
    print("Should be 99: ", hm["apple"])

    print("\n--Test 3--")
    del hm["banana"]
    print("Should be False: ", "banana" in hm)

    print("\n--Test 4--")
    print("Should be True: ", "apple" in hm)
    print("Should be False: ", "banana" in hm)

    print("\n--Test 5--")
    hm["one"] = 1
    hm["two"] = 2
    hm["three"] = 3
    print("Should be 1: ", hm["one"])
    print("Should be 2: ", hm["two"])
    print("Should be 3: ", hm["three"])

    print("\n--Test 6--")
    keys = hm.get_keys()
    print("Keys in hashmap: ", keys)