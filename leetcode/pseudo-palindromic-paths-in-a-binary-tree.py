# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # Dictionary to count frequency of each digit in the current path
        count = defaultdict(int)
        # Tracks how many digits currently appear an odd number of times
        odd = 0

        def dfs(node):
            nonlocal odd  # allow modifying the outer variable 'odd'
            if not node:
                return 0  # Base case: no path through a null node
            
            # Include this node's value in the path frequency
            count[node.val] += 1

            # Check if this digit just became odd-count or even-count
            # If count is odd, odd_change = +1; if even, odd_change = -1
            odd_change = 1 if count[node.val] % 2 == 1 else -1
            odd += odd_change

            # If we're at a leaf node:
            if not node.left and not node.right:
                # A path is pseudo-palindromic if at most 1 digit has an odd frequency
                res = 1 if odd <= 1 else 0
            
            else:
                # Otherwise, continue DFS down left and right subtrees
                res = dfs(node.left) + dfs(node.right)
            
            # Backtrack: undo the changes before returning
            odd -= odd_change
            count[node.val] -= 1

            return res

        # Start DFS traversal from root
        return dfs(root)