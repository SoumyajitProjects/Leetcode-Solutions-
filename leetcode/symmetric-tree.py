# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Iterative BFS solution:
        if not root:
            return True
        
        q = deque([(root.left, root.right)])
        while q:
            l , r = q.popleft()
            
            if not l and not r:
                continue
            if not l or not r or l.val != r.val:
                return False
            
            q.append((l.left, r.right))
            q.append((l.right , r.left))
        return True


        """
        Recurisve DFS Solution:

        # If the tree is empty, it's symmetric by definition
        if not root:
            return True
        
        # Depth-First Search helper function
        # Takes two nodes (l and r) and checks if they are mirror images
        def dfs(l, r):
            # Case 1: Both nodes are None → symmetric at this branch
            if not l and not r:
                return True
            
            # Case 2: One node is None OR values don’t match → not symmetric
            if not l or not r or l.val != r.val:
                return False
            
            # Case 3: Recursive check:
            # Compare left child of l with right child of r
            # Compare right child of l with left child of r
            return (
                dfs(l.left, r.right) and 
                dfs(l.right, r.left)
            )
        
        # Initial call: check left and right subtrees of root
        return dfs(root.left, root.right)
        """