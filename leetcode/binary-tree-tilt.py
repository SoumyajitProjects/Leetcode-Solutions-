# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tilt = 0

        def dfs(node):
            if not node:
                return 0
            
            # Recursively compute left and right subtree sums
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            
            # Add the tilt of the current node to the total tilt
            self.tilt += abs(leftSum - rightSum)
            
            # Return the sum of the subtree including current node
            return leftSum + rightSum + node.val

        dfs(root)
        return self.tilt