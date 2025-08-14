# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Dummy simplifies edge handling (reversing first group)
        dummy = ListNode(0, head)
        groupPrev = dummy  # node before the current k-group

        while True:
            # Find the kth node from groupPrev (the tail of this k-group)
            kth = self.getKth(groupPrev, k)
            if not kth:
                # Fewer than k nodes remain → stop (leave remainder as-is)
                break
            groupNext = kth.next  # node just after the k-group

            # Reverse the nodes in [groupPrev.next, kth] inclusive
            prev, curr = groupNext, groupPrev.next
            # Standard in-place reversal until we pass groupNext
            while curr != groupNext:
                temp = curr.next      # save next
                curr.next = prev      # reverse link
                prev = curr           # advance prev
                curr = temp           # advance curr

            # After reversal:
            # - prev points to the new head of this group (which is 'kth')
            # - groupPrev.next was old head, now it's the tail of the group
            # Reconnect groupPrev to the new head (kth), and move groupPrev to tail
            temp = groupPrev.next    # old head -> now tail of the reversed group
            groupPrev.next = kth     # hook previous segment to new group head
            groupPrev = temp         # advance to tail to start next group

        return dummy.next

    def getKth(self, curr, k):
        # Move k steps from curr; return the kth node ahead (or None if not enough nodes)
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr