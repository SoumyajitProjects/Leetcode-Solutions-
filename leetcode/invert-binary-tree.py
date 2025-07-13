# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Base case: if the current node is None, there's nothing to invert
        if not root:
            return None
        
        # Swap the left and right children of the current node
        root.left, root.right = root.right, root.left       

        # Recursively invert the left subtree (which was originally the right)
        self.invertTree(root.left)

        # Recursively invert the right subtree (which was originally the left)
        self.invertTree(root.right)

        # Return the current node after its subtree has been inverted
        return root