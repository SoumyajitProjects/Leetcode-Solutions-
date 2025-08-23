# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base case: if the tree is empty (root is None),
        # create a new node with the given value and return it
        if not root:
            return TreeNode(val)
        
        # If val is greater than the current node's value,
        # go to the right subtree and insert there
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        
        # If val is smaller (or equal, though in BST duplicates
        # usually go left by convention), go to the left subtree
        else:
            root.left = self.insertIntoBST(root.left, val)
        
        # Return the root node after insertion so that parent nodes
        # can correctly reconnect the subtree during recursion
        return root