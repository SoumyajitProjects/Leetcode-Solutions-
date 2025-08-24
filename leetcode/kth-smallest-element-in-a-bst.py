# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res = []  # List to store nodes in sorted order (from inorder traversal)

        # Helper function to perform inorder traversal (Left → Root → Right)
        def inorder(node):
            # Base case: if the node is None, return immediately
            if not node:
                return

            # Recurse into the left subtree
            inorder(node.left)

            # Process the current node (in inorder, this means adding to sorted list)
            res.append(node.val)

            # Recurse into the right subtree
            inorder(node.right)

        # Start inorder traversal from the root
        inorder(root)

        # Since inorder traversal of a BST gives sorted order,
        # the kth smallest element is at index k-1
        return res[k - 1]


        """
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
        """