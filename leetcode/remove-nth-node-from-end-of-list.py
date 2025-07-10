# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize two pointers both at the head
        fast = head
        slow = head

        # Step 1: Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # Edge case: if fast is None after moving n steps, it means
        # we're deleting the head node (length == n)
        if not fast:
            return head.next

        # Step 2: Move both pointers until fast reaches the last node
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Step 3: Skip the node after slow (i.e. delete nth node from end)
        slow.next = slow.next.next

        return head