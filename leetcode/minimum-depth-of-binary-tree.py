# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        # Iterative Solution 
        if not root:
            return 0
        
        # Queue stores pairs: (node, depth)
        q = deque([(root, 1)])
        
        while q:
            node, depth = q.popleft()
            
            # If this node is a leaf, we found the minimum depth
            if not node.left and not node.right:
                return depth
            
            # Push left child with depth+1
            if node.left:
                q.append((node.left, depth + 1))
            
            # Push right child with depth+1
            if node.right:
                q.append((node.right, depth + 1))
        """ 
        Recursive DFS Solution
        # Base case: If the tree is empty, depth is 0
        if not root:
            return 0
        
        # If the left child is missing, 
        # the minimum depth must come from the right subtree
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        # If the right child is missing, 
        # the minimum depth must come from the left subtree
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # If both children exist, 
        # take the minimum depth of the two subtrees
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        """