# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Base case: if the input list is empty, return None
        if not lists or len(lists) == 0:
            return None
        
        # Continue merging lists until there is only one list left
        while len(lists) > 1:
            mergedLists = []

            # Merge pairs of lists (0 with 1, 2 with 3, etc.)
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # Handle odd number of lists by pairing last one with None
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                # Merge the two lists and add the result to mergedLists
                mergedLists.append(self.mergeList(l1, l2))

            # Replace original lists with merged results for the next round
            lists = mergedLists

        # The final remaining list is the fully merged k lists
        return lists[0]
    
    # Helper function to merge two sorted linked lists (same as in mergeTwoLists)
    def mergeList(self, l1, l2):
        # Dummy node to simplify edge cases
        dummy = ListNode()
        tail = dummy 

        # Merge nodes from l1 and l2 in sorted order
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1       # attach l1 node
                l1 = l1.next         # move l1 forward
            else:
                tail.next = l2       # attach l2 node
                l2 = l2.next         # move l2 forward
            tail = tail.next         # move tail forward

        # Attach any remaining nodes from l1 or l2
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        # Return the merged list (skipping the dummy node)
        return dummy.next