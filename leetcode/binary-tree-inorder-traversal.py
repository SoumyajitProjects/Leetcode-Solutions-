# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val           # Value of the node
#         self.left = left         # Pointer/reference to the left child
#         self.right = right       # Pointer/reference to the right child

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []        # List to store the inorder traversal result
        stack = []      # Stack to simulate the recursion (store nodes temporarily)
        curr = root     # Start traversal from the root node

        # Continue until all nodes are processed
        # Either there are nodes left to visit (`curr`) or nodes in the stack
        while curr or stack:
            
            # Step 1: Traverse as far left as possible
            # Push nodes onto the stack while moving left
            while curr:
                stack.append(curr)   # Save current node to come back later
                curr = curr.left     # Move to left child
            
            # Step 2: Process the node at the top of the stack
            curr = stack.pop()       # Pop the most recent node we visited
            res.append(curr.val)     # Visit the node (add its value to result)
            
            # Step 3: Move to the right subtree
            curr = curr.right        # Now, traverse the right child of this node

        return res  # Return the inorder traversal list


        """
        Recurisve Solution
        res = []  # This list will store the inorder traversal result

        # Define a helper recursive function to perform inorder traversal
        def inorder(root):
            if not root:  # Base case: if the node is None, just return
                return 
            
            inorder(root.left)        # Step 1: Traverse the left subtree
            res.append(root.val)      # Step 2: Visit the current node (append its value)
            inorder(root.right)       # Step 3: Traverse the right subtree

        inorder(root)  # Start the traversal from the root node
        return res     # Return the list of visited nodes in inorder order
        """