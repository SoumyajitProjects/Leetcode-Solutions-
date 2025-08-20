# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # Iterative BFS Solution 
        queue = deque([(p, q)])

        while queue:
            a, b = queue.popleft()

            if not a and not b:
                continue                   # both empty at this spot → OK
            if not a or not b or a.val != b.val:
                return False               # one empty, one not or values do not match

            # enqueue children in the same order
            queue.append((a.left,  b.left))
            queue.append((a.right, b.right))

        return True
            


        """
        Recursive DFS Solution:

        # If both nodes are None, the trees are structurally identical at this branch
        if not p and not q:
            return True
        
        # If one node is None and the other is not, or if the values don't match,
        # the trees are not the same
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check the left and right subtrees of both trees
        return (
            self.isSameTree(p.left, q.left) and  # Check left subtree
            self.isSameTree(p.right, q.right)    # Check right subtree
        )
        """