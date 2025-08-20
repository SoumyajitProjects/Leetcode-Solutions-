# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty, return an empty list
        if not root:
            return []
        
        res = []                         # Final result list to store zigzag levels
        q = collections.deque()          # Queue for BFS traversal
        q.append(root)                   # Start BFS with the root node

        # Process nodes level by level
        while q:
            level = []                   # Stores values for the current level
            
            # Iterate through all nodes currently in the queue (one level)
            for i in range(len(q)):
                node = q.popleft()       # Pop from the left (FIFO behavior)
                level.append(node.val)   # Add the node’s value to the current level

                # Add child nodes to the queue for the next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # If we are on an odd level (1-indexed), reverse the order of values
            if len(res) % 2 == 1:        # res already has some levels → odd/even check
                level = list(reversed(level))
            
            # Append the processed level into the result
            res.append(level)
        
        # Return the final zigzag level order traversal
        return res