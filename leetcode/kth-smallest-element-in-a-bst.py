# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Stack to simulate in-order traversal iteratively
        stack = []
        curr = root
        n = 0  # Counter for how many nodes we've visited in-order

        # Continue while there are nodes to process
        while stack or curr:
            # Traverse as left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Pop from stack (next smallest element)
            curr = stack.pop()
            n += 1  # Increment count of visited nodes

            # If this is the k-th node we've seen, return its value
            if n == k:
                return curr.val

            # Move to the right child to continue traversal
            curr = curr.right