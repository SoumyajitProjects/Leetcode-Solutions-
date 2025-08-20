# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize a variable to keep track of the maximum diameter found so far
        self.diameter = 0

        def dfs(root):
            """
            A recursive DFS function that computes:
            1. The height of each subtree.
            2. Updates the diameter if the path through the current node is larger.
            """
            if not root:  # Base case: if the node is None, height = 0
                return 0
            
            # Recursively calculate left and right subtree heights
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)

            # The longest path through the current node = leftHeight + rightHeight
            # Update the global diameter if this path is longer
            self.diameter = max(self.diameter, leftHeight + rightHeight)

            # Return the height of the current node = 1 + max of child heights
            return 1 + max(leftHeight, rightHeight)

        # Start DFS from root
        dfs(root)

        # Return the final maximum diameter found
        return self.diameter