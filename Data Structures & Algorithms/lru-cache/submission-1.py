class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.leftNode = Node(0, 0)
        self.rightNode = Node(0, 0)
        self.mp = {}
        self.leftNode.next, self.rightNode.prev = self.rightNode, self.leftNode

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev, nxt = self.rightNode.prev, self.rightNode
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.mp:
            self.remove(self.mp[key])
            self.insert(self.mp[key])
            return self.mp[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.remove(self.mp[key])
        self.mp[key] = Node(key, value)
        self.insert(self.mp[key])

        if len(self.mp) > self.capacity:
            lru  = self.leftNode.next
            self.remove(lru)
            del self.mp[lru.key]
        return
