# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty, return an empty list
        if not root:
            return []
        
        res = []  # Final result to hold levels of nodes
        q = collections.deque()  # Queue to perform BFS (breadth-first search)
        q.append(root)  # Start BFS from the root node

        # Standard BFS loop
        while q:
            level = []  # List to hold values of the current level
            # Process all nodes currently in the queue (i.e., one level at a time)
            for i in range(len(q)):
                node = q.popleft()  # Pop node from the left of the queue
                level.append(node.val)  # Add its value to the current level
                
                # Enqueue left child if it exists
                if node.left:
                    q.append(node.left)
                # Enqueue right child if it exists
                if node.right:
                    q.append(node.right)
            
            # After finishing this level, add it to the result
            res.append(level)
        
        # Since we collected levels from top-to-bottom, reverse to get bottom-to-top
        return list(reversed(res))