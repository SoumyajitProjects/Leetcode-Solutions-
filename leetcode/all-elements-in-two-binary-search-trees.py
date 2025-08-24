# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        self.res = []  # List to store all node values from both trees

        # Preorder traversal for the first tree
        def preorder1(node1):
            if not node1:
                return None
            # Visit root first
            self.res.append(node1.val)
            # Traverse left subtree
            preorder1(node1.left)
            # Traverse right subtree
            preorder1(node1.right)
        preorder1(root1)

        # Preorder traversal for the second tree
        def preorder2(node2):
            if not node2:
                return None
            # Visit root first
            self.res.append(node2.val)
            preorder2(node2.left)
            preorder2(node2.right)
        preorder2(root2)

        # Sort all collected values since preorder doesn't give sorted order
        return sorted(self.res)