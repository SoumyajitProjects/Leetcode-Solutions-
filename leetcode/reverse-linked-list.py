# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val         # Value stored in the node
#         self.next = next       # Pointer to the next node in the list

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None              # 'prev' will eventually become the new head (start as None)
        curr = head              # 'curr' starts at the current head of the list

        # Traverse the entire linked list
        while curr:
            forward = curr.next  # Save the next node to move forward later
            curr.next = prev     # Reverse the link: point current node back to 'prev'
            prev = curr          # Move 'prev' one step forward (to current node)
            curr = forward       # Move 'curr' one step forward (to saved 'forward')

        return prev              # At the end, 'prev' will be the new head of the reversed list