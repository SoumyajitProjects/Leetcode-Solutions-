# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.res = 0   # Counter to keep track of the number of good nodes

        # Depth-First Search helper function
        # node → current node
        # max_node → maximum value seen so far on the path from the root
        def dfs(node, max_node):
            # Base case: if node is None, stop recursion
            if not node:
                return 0
            
            # If current node's value is >= maximum value seen so far,
            # then this node is a "good node"
            if node.val >= max_node:
                self.res += 1   # Increment good node counter
            
            # Recurse on left and right subtrees
            # Update max_node with the larger of current node value and previous max
            dfs(node.left, max(max_node, node.val))
            dfs(node.right, max(max_node, node.val))
        
        # Start DFS traversal from root, with root's value as the initial max
        dfs(root, root.val)

        # Return the total number of good nodes found
        return self.res