# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        # Initialize the m x n matrix with -1 (default fill value)
        res = [[-1] * n for _ in range(m)]

        # Boundaries for the spiral traversal
        left, right = 0, n          # columns: [left, right)
        top, bottom = 0, m          # rows: [top, bottom)

        # Continue as long as there are nodes left in the linked list
        while head:

            # 1. Fill the top row from left to right
            for i in range(left, right):
                if not head:        # If we run out of nodes, return matrix
                    return res
                res[top][i] = head.val
                head = head.next
            top += 1                # Move top boundary downward

            # 2. Fill the right column from top to bottom
            for i in range(top, bottom):
                if not head:
                    return res
                res[i][right - 1] = head.val
                head = head.next
            right -= 1              # Move right boundary left

            # 3. Fill the bottom row from right to left
            for i in range(right - 1, left - 1, -1):
                if not head:
                    return res
                res[bottom - 1][i] = head.val
                head = head.next
            bottom -= 1             # Move bottom boundary upward

            # 4. Fill the left column from bottom to top
            for i in range(bottom - 1, top - 1, -1):
                if not head:
                    return res
                res[i][left] = head.val
                head = head.next
            left += 1               # Move left boundary right
        
        # Return result once all nodes are consumed
        return res