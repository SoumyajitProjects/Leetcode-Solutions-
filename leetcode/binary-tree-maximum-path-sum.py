# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize the result with the value of the root node
        # This will keep track of the maximum path sum found so far
        res = [root.val]

        # Define a recursive DFS helper function
        def dfs(root):
            # Base case: if we hit a null node, return 0
            if not root:
                return 0 
            
            # Recursively compute the max path sum from the left and right subtrees
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # Ignore negative contributions; treat them as 0
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Update the global max path sum if the current path through the node is higher
            # This considers splitting at the current root (taking both left and right)
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # Return the max gain if we continue the path through only one child (not split)
            return root.val + max(leftMax, rightMax)

        # Start DFS traversal from the root
        dfs(root)

        # Return the maximum path sum found
        return res[0]