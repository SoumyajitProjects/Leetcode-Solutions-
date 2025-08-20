# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visit = [False]   # False = first time seen, True = process node value
        res = []

        while stack:
            cur, v = stack.pop(), visit.pop()
            if cur:
                if v:
                    # Second time we see this node: both children have been handled
                    res.append(cur.val)
                else:
                    # Postorder: left, right, node
                    # Push current back as visited
                    stack.append(cur)
                    visit.append(True)

                    # Push right child (unvisited)
                    stack.append(cur.right)
                    visit.append(False)

                    # Push left child (unvisited)
                    stack.append(cur.left)
                    visit.append(False)

        return res

        """
        Recursive Solution:

        # This list will store the traversal result
        res = []

        # Define a helper function for recursive postorder traversal
        def postorder(root):
            # Base case: if the current node is None, return immediately
            if not root:
                return 

            # Step 1: Traverse the left subtree
            postorder(root.left)
            # Step 2: Traverse the right subtree
            postorder(root.right)
            # Step 3: Process the current node (append its value to result)
            res.append(root.val)

        # Start recursion from the root node
        postorder(root)
        
        # Return the final traversal result
        return res
        """