# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        i = 0
        size = 0
        
        while cur:
            size += 1
            cur = cur.next
        
        n = size - n
        cur = dummy

        for i in range(n-1):
            cur = cur.next

        cur.next = cur.next.next

        return dummy.next
