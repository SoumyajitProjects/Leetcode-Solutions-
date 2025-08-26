# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        # This will store all valid root-to-leaf paths that sum to targetSum
        self.res = []

        def dfs(node, curr_sum, path):
            # Base case: if node is None, return (no work to do)
            if not node:
                return None
            
            # Add current node's value to the running sum
            curr_sum += node.val
            # Add current node's value to the current path
            temp = path + [node.val]

            # Explore the left subtree if it exists
            if node.left:
                dfs(node.left, curr_sum, temp)
            
            # Explore the right subtree if it exists
            if node.right:
                dfs(node.right, curr_sum, temp)
            
            # If it's a leaf node (no children) AND the sum equals targetSum
            if not node.left and not node.right and curr_sum == targetSum:
                # Append this valid path to results
                self.res.append(temp)
        
        # Start DFS from the root, with sum = 0 and empty path
        dfs(root, 0, [])
        # Return all collected valid paths
        return self.res