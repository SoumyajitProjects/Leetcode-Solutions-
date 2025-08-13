"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Hash map from original node -> copied node
        # Seed with {None: None} so we can write `oldToCopy[cur.next]` / `oldToCopy[cur.random]`
        # without checking for None each time.
        oldToCopy = {None: None}

        # 1) First pass: create a copy node for every original node (values only)
        cur = head
        while cur:
            copy = Node(cur.val)       # new node with same value
            oldToCopy[cur] = copy      # map original -> copy
            cur = cur.next

        # 2) Second pass: wire up next and random pointers using the map
        cur = head
        while cur:
            copy = oldToCopy[cur]              # the clone of current original
            copy.next = oldToCopy[cur.next]    # clone's next = clone of original's next
            copy.random = oldToCopy[cur.random]# clone's random = clone of original's random
            cur = cur.next

        # Return the head of the cloned list
        return oldToCopy[head]