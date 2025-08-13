# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy head to simplify list construction (avoids handling head as a special case)
        dummy = ListNode()
        cur = dummy  # tail pointer of the result list

        carry = 0    # carry from the previous digit addition

        # Continue while at least one list has nodes left or there is a carry to place
        while l1 or l2 or carry:
            # Current digit values (0 if the list is exhausted)
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Add the two digits plus incoming carry
            val = v1 + v2 + carry

            # Compute new carry and the digit to store in the current node
            carry = val // 10         # carry is 1 if val >= 10, else 0
            val = val % 10            # current digit (0..9)

            # Append the new digit node to the result list
            cur.next = ListNode(val)
            cur = cur.next

            # Advance input list pointers if possible
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # The result list starts at dummy.next (skip dummy node)
        return dummy.next