# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        temp = head

        while temp:
            if temp.val < x:
                cur.next = ListNode(temp.val)
                cur = cur.next
            temp = temp.next
        
        temp = head

        while temp:
            if temp.val >= x:
                cur.next = ListNode(temp.val)
                cur = cur.next
            temp = temp.next
        
        return dummy.next
        