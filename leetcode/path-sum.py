# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Depth-first search helper function
        def dfs(node, curr_sum):
            if not node:
                # If we reach a null node, no path exists here
                return False
            
            # Add current node's value to running sum
            curr_sum += node.val
            
            # If it's a leaf node (no left or right children)
            # check if the accumulated sum equals targetSum
            if not node.left and not node.right:
                return curr_sum == targetSum
            
            # Otherwise, continue DFS on left or right child
            # If either subtree returns True, path exists
            return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)
        
        # Start DFS from the root with sum = 0
        return dfs(root, 0)