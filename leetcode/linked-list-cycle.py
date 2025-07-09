# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers: slow moves 1 step, fast moves 2 steps
        slow, fast = head, head

        # Traverse the list until fast pointer reaches the end
        while fast and fast.next:
            slow = slow.next            # Move slow pointer one step
            fast = fast.next.next       # Move fast pointer two steps

            # If both pointers meet, there's a cycle
            if slow == fast:
                return True

        # If we reach here, fast hit the end -> no cycle
        return False