class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> Node

        # Sentinel (dummy) nodes for the doubly linked list:
        # left  = LRU end (least recently used lives next to left)
        # right = MRU end (most recently used is inserted just before right)
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # Remove a node from the DLL in O(1)
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Insert a node right before `right` (mark as MRU) in O(1)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    # Get value; promote node to MRU if present
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move to MRU position: delete from current spot, insert near right
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    # Put key/value:
    # - If key exists, remove old node (we'll re-insert with new value).
    # - Insert as MRU.
    # - If over capacity, evict LRU (node next to `left`) from both DLL and map.
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next         # the least recently used node
            self.remove(lru)             # evict from list
            del self.cache[lru.key]      # evict from hashmap