class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            # Base case: an empty subtree is balanced with height 0
            if not root:
                return [True, 0]
            
            # Recursively check left and right subtrees
            left, right = dfs(root.left), dfs(root.right)
            
            # A node is balanced if:
            # 1. Both left and right subtrees are balanced
            # 2. The height difference between them is <= 1
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)       
            
            # Return:
            # - Whether this subtree is balanced
            # - Height of this subtree = 1 + max(left height, right height)
            return [balanced, 1 + max(left[1], right[1])]
        
        # Final answer: only return the balanced status
        return dfs(root)[0]