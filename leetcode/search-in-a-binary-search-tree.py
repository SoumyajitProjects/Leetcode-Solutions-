# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
       current = root
        
        while current:
            if current.val == val:   # Found the node
                return current
            elif val < current.val:  # Search left
                current = current.left
            else:                    # Search right
                current = current.right
        
        return None  # If not found
        """
        # Base case: if root is None or we found the node with value == val
        if not root or root.val == val:
            return root

        # If val is smaller, search in the left subtree
        if val < root.val:
            return self.searchBST(root.left, val)
        
        # If val is larger, search in the right subtree
        return self.searchBST(root.right, val)
        """