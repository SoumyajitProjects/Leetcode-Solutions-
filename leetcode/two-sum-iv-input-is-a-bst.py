# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        
        seen = set()                 # store visited node values
        queue = deque([root])        # BFS queue
        
        while queue:
            node = queue.popleft()

            # Check if complement exists
            if k - node.val in seen:
                return True
            
            seen.add(node.val)

            # Push children to queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False


        """
        Recursive Solution:

        seen = set()   # keep track of visited node values

        def dfs(node):
            if not node:
                return False

            # Check if complement already exists
            if k - node.val in seen:
                return True
            
            # Add current value to set
            seen.add(node.val)

            # Keep searching in left and right subtrees
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
        """