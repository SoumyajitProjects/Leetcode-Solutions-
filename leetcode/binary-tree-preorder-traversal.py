# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []        # Result list to store the preorder traversal values
        stack = []      # Stack to keep track of right children that need to be processed later
        cur = root      # Start traversal at the root node

        while cur or stack:   # Continue while there is a current node OR something in the stack
            if cur:
                # Preorder → Visit node first
                res.append(cur.val)

                # Push the right child (if any) onto the stack to process later
                stack.append(cur.right)

                # Move left (priority to left child in preorder)
                cur = cur.left
            else:
                # If no current node, pop from stack → this brings back the last saved right child
                cur = stack.pop()

        return res

       
        
            

        """
        res = []   # This list will store the traversal result in preorder order

        # Define a helper function for recursive preorder traversal
        def preorder(root):
            if not root:    # Base case: if the current node is None, just return
                return 
            
            # Step 1: Visit the current node
            res.append(root.val)
            
            # Step 2: Recursively traverse the left subtree
            preorder(root.left)
            
            # Step 3: Recursively traverse the right subtree
            preorder(root.right)

        # Call the helper function starting from the root
        preorder(root)
        
        # Return the final preorder traversal result
        return res
        """