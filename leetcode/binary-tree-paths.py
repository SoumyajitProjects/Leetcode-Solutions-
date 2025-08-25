# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # Result list to store all root-to-leaf paths
        res = []

        # Depth-first search (DFS) helper function
        def dfs(node, path):
            if not node:  
                # If node is None, stop recursion
                return 
            
            # If the node is a leaf (no children), 
            # add the completed path to the result list
            if not node.left and not node.right:
                res.append(path + str(node.val))
                return 
            
            # If the node has a left child, continue DFS
            # Add the current node value + "->" to the path string
            dfs(node.left , path + str(node.val) + "->")
            
            # If the node has a right child, continue DFS
            dfs(node.right , path + str(node.val) + "->")
        
        # Start DFS from the root with an empty path
        dfs(root , "")
        
        # Return the list of all root-to-leaf paths
        return res