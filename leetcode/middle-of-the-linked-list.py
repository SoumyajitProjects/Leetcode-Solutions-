# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val         # Value stored in the node
#         self.next = next       # Pointer to the next node in the list

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers: 'slow' and 'fast'
        slow, fast = head, head

        # Move 'fast' two steps and 'slow' one step at a time
        # When 'fast' reaches the end, 'slow' will be at the middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # 'slow' now points to the middle node
        return slow