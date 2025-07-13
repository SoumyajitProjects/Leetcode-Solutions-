# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        # If t is None, it's trivially a subtree of any tree
        if not t:
            return True
        # If s is None but t is not, t can't be a subtree
        if not s:
            return False
        
        # If the current roots are the same, check if their entire trees match
        if self.sameTree(s, t):
            return True
        
        # Otherwise, recursively check if t is a subtree of s's left or right child
        return (self.isSubtree(s.left, t) or self.isSubtree(s.right, t))
    
    def sameTree(self, s, t):
        # If both trees are empty, they match
        if not s and not t:
            return True
        
        # If one is empty or the values don't match, return False
        if not s or not t or s.val != t.val:
            return False
        
        # Recursively check if both left and right subtrees match
        return (self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right))