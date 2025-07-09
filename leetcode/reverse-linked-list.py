# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize previous pointer as None (end of reversed list)
        prev = None

        # Start from the head of the original list
        curr = head

        # Iterate through the linked list
        while curr:
            # Save the next node before breaking the link
            next_node = curr.next

            # Reverse the current node's pointer
            curr.next = prev

            # Move the 'prev' pointer one step forward (to current)
            prev = curr

            # Move to the next node in the original list
            curr = next_node

        # At the end, prev is the new head of the reversed list
        return prev