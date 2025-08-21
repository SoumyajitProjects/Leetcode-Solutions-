# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None                # Store previous node value during in-order traversal
        self.min_diff = float("inf")    # Start with infinity (since we want to minimize)

        def inorder(node):
            if not node:
                return
            # 1. Traverse left subtree
            inorder(node.left)

            # 2. Process current node
            if self.prev is not None:   # If a previous node exists, calculate difference
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val        # Update prev to current node value

            # 3. Traverse right subtree
            inorder(node.right)

        inorder(root)
        return self.min_diff