# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty, return an empty list
        if not root:
            return []
        
        res = []                          # Final result: list of levels
        q = collections.deque()           # Queue to support BFS
        q.append(root)                    # Start with the root node

        # Process nodes level by level
        while q:
            level = []                    # Temporary list to store current level
            for i in range(len(q)):       # Number of nodes in this level
                node = q.popleft()        # Dequeue the next node
                level.append(node.val)    # Add the node's value to current level
                
                # Enqueue children for the next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # Append the completed level to result
            if level:
                res.append(level)
        
        return res                        # Return all levels