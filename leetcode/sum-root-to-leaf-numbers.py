# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        # Depth-First Search helper function
        def dfs(node, curr_sum):
            # Base case: if node is None, return 0 (no contribution)
            if not node:
                return 0
            
            # Update the running sum by shifting previous digits left (*10)
            # and adding the current node's value
            curr_sum = curr_sum * 10 + node.val

            # If it's a leaf node (no children), return the number formed
            if not node.left and not node.right:
                return curr_sum
            
            # Otherwise, continue exploring left and right subtrees
            # and return their total sum
            return dfs(node.left, curr_sum) + dfs(node.right, curr_sum)
        
        # Start DFS from root with initial sum = 0
        return dfs(root, 0)