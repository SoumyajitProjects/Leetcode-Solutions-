# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # If value < low → discard left subtree, recurse right
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        # If value > high → discard right subtree, recurse left
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        # Otherwise, fix both subtrees
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        return root