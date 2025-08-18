class Solution:
    def deleteNode(self, node: ListNode) -> None:
        # Copy the next node's value into this node
        node.val = node.next.val
        # Bypass the next node
        node.next = node.next.next