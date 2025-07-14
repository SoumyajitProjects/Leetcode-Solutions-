# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Result list to store the values at each level
        res = []

        # Initialize a queue using deque for BFS traversal
        q = collections.deque()
        q.append(root)  # Start with the root node

        # Loop until the queue is empty
        while q:
            qLen = len(q)  # Number of nodes at the current level
            level = []     # List to store values at this level

            # Process all nodes at the current level
            for i in range(qLen):
                node = q.popleft()  # Pop the node from the left of the queue
                if node:
                    level.append(node.val)      # Add node's value to the level list
                    q.append(node.left)         # Add left child to queue (even if None)
                    q.append(node.right)        # Add right child to queue (even if None)

            # Only add non-empty levels to the result
            if level:
                res.append(level)

        return res  # Return the list of levels