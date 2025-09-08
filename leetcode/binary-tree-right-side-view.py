from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Edge case: if the tree is empty, return an empty list
        if not root:
            return []
        
        res = []                # list to store the final right side view
        q = deque([root])       # queue for BFS, initialized with the root

        # Standard BFS loop
        while q:
            rightSide = None    # variable to track the rightmost node of the current level
            qLen = len(q)       # number of nodes in the current level

            # Process all nodes at the current level
            for i in range(qLen):
                node = q.popleft()   # pop from the left of the queue

                if node:
                    rightSide = node   # update rightSide; the last update will be the rightmost

                    # Add children to the queue for the next level
                    q.append(node.left)
                    q.append(node.right)
            
            # After finishing this level, rightSide holds the rightmost node
            if rightSide:
                res.append(rightSide.val)
        
        # Return the list of rightmost nodes, level by level
        return res