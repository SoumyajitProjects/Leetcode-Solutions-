# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def search(node):
            if not node:
                return None
            
            # If the key is smaller, go left
            if key < node.val:
                node.left = search(node.left)
            
            # If the key is bigger, go right
            elif key > node.val:
                node.right = search(node.right)
            
            # Found the node to delete
            else:
                # Case 1: Node to delete has no children
                if not node.left and not node.right:
                    return None
                
                # Case 2: Node to delete has one child
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                
                # Case 3: Node to delete has 2 children
                # Find the inorder successor (smallest in right subtree)
                successor = node.right
                while successor.left:
                    successor = successor.left
                
                # Replace node's value with successor's value
                node.val = successor.val
                
                # Delete the successor node from the right subtree
                node.right = self.deleteNode(node.right, successor.val)
            
            return node
        
        return search(root)