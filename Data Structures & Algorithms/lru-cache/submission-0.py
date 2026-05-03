class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap, self.length = capacity, 0
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        self.map = {}

    def insert(self, node: Optional[Node]):
        prev, next = self.right.prev, self.right
        prev.next, next.prev = node, node
        node.prev, node.next = prev, next

    def remove(self, node: Optional[Node]):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.map[key] = node
            self.insert(node)
            self.length += 1
            if self.length > self.cap:
                self.map.pop(self.left.next.key)
                self.remove(self.left.next)
                self.length -= 1


