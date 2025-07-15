# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function to validate the BST property for a subtree
        def valid(node, left, right):
            # An empty node is always valid
            if not node:
                return True
            
            # If current node violates the BST rule, return False
            # Each node must be strictly > left bound and < right bound
            if not (node.val < right and node.val > left):
                return False
            
            # Recursively check left and right subtrees with updated bounds
            return (
                valid(node.left, left, node.val) and     # Left subtree: values must be < current node
                valid(node.right, node.val, right)       # Right subtree: values must be > current node
            )
        
        # Initial call with infinite bounds for the root
        return valid(root, float("-inf"), float("inf"))