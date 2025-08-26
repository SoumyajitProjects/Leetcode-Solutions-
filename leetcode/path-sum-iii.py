# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Variable to store the total number of valid paths
        self.total = 0
        # Hashmap to count prefix sums (how many times each sum occurs)
        self.lookup = defaultdict(int)
        
        # Initialize with targetSum so paths starting from root are counted
        self.lookup[targetSum] = 1

        def dfs(node, curr_sum):
            if not node:
                return 
            
            # Update running prefix sum with current node value
            curr_sum += node.val

            # If there was a prefix sum such that (curr_sum - prefix) = targetSum,
            # then we have found valid path(s). This is pre-counted in lookup.
            self.total += self.lookup[curr_sum]

            # Add future "needed" sum into lookup (curr_sum + targetSum).
            # This means if we later reach a prefix sum equal to this,
            # we'll know we found a valid path.
            self.lookup[curr_sum + targetSum] += 1

            # Continue DFS down both children
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)

            # Backtrack: remove the current path's contribution
            self.lookup[curr_sum + targetSum] -= 1
        
        # Start DFS from root with sum = 0
        dfs(root, 0)
        return self.total