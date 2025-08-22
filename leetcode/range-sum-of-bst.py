from collections import deque

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Initialize a variable to keep track of the running sum
        self.sum = 0

        # Define a helper function to perform DFS (preorder traversal)
        def preorder(node):
            # Base case: if the node is None, return immediately
            if not node:
                return 0
            
            # If the current node's value lies within [low, high], add it to sum
            if low <= node.val <= high:
                self.sum += node.val
            
            # Continue DFS into the left subtree
            preorder(node.left)
            
            # Continue DFS into the right subtree
            preorder(node.right)

        # Start preorder DFS from the root
        preorder(root)

        # Return the accumulated sum of values within [low, high]
        return self.sum



        """
        Iteravtive Solution:
        
        # Edge case: if the tree is empty, return 0
        if not root:
            return 0
        
        sum = 0  # to accumulate the sum of valid node values
        q = deque([root])  # queue for BFS traversal, start with root node

        # Standard BFS loop
        while q:
            node = q.popleft()  # pop the current node from the left of the queue

            # If the current node's value lies within the range [low, high],
            # add it to the running total
            if low <= node.val <= high:
                sum += node.val
            
            # Push left child into the queue if it exists
            # (we don't prune here, so BFS visits all nodes)
            if node.left:
                q.append(node.left)
            
            # Push right child into the queue if it exists
            if node.right:
                q.append(node.right)
        
        # Return the final sum after traversing the tree
        return sum
        """