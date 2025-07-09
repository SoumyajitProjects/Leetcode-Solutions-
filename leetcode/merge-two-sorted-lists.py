# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create a dummy node to serve as the starting point of the merged list
        dummy = ListNode()
        
        # 'tail' will always point to the last node in the merged list
        tail = dummy 

        # Traverse both lists until one is exhausted
        while list1 and list2:
            # If the current node in list1 is smaller, append it to the merged list
            if list1.val < list2.val:
                tail.next = list1     # Link the smaller node
                list1 = list1.next    # Move list1 forward
            else:
                # Otherwise, append the node from list2
                tail.next = list2
                list2 = list2.next    # Move list2 forward
            tail = tail.next          # Advance the tail to the newly added node
        
        # At this point, one of the lists is exhausted.
        # Append the remaining part of the non-empty list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        # The merged list starts from dummy.next (skipping the initial dummy node)
        return dummy.next