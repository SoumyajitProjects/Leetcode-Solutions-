# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []  # List to store the serialized tree values

        def dfs(node):
            if not node:
                # If the node is null, use "N" to represent null nodes
                res.append("N")
                return
            # Append the current node's value to the result list
            res.append(str(node.val))
            # Recurse on the left subtree
            dfs(node.left)
            # Recurse on the right subtree
            dfs(node.right)

        dfs(root)  # Start DFS from root
        # Join all values in the list using commas to create a single string
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")  # Split the serialized string into a list of values
        self.i = 0  # Pointer to track position during recursive reconstruction

        def dfs():
            # Base case: if we encounter a "N", it's a null node
            if vals[self.i] == "N":
                self.i += 1  # Move to the next value
                return None
            # Create a TreeNode from the current value
            node = TreeNode(int(vals[self.i]))
            self.i += 1  # Move to the next value
            # Recursively build the left subtree
            node.left = dfs()
            # Recursively build the right subtree
            node.right = dfs()
            return node  # Return the constructed subtree rooted at `node`
        
        return dfs()  # Start deserialization from index 0