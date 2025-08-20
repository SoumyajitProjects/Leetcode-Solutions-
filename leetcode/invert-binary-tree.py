# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Initialize a queue for BFS
        queue = deque([root])

        while queue:
            node = queue.popleft()  # Process current node

            # Swap children of current node
            node.left, node.right = node.right, node.left

            # Add children to queue if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root


        """
        Recurisve Solution:

        # Base case: if the node is None, return None (empty tree or end of branch)
        if not root:
            return None
        
        # Swap the left and right child pointers of the current node
        root.left, root.right = root.right, root.left

        # Recursively invert the left subtree (which was originally the right subtree)
        self.invertTree(root.left)

        # Recursively invert the right subtree (which was originally the left subtree)
        self.invertTree(root.right)

        # Return the root of the inverted tree
        return root
        """