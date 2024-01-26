# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            cur = head.next
            head.next = prev
            prev = head
            head = cur
        
        return prev

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1 

        dummy1 = ListNode()
        cur1 = dummy1

        dummy2 = ListNode()
        cur2 = dummy2

        dummy3 = ListNode()
        cur3 = dummy3

        cur = head

        while count < left:
            cur1.next = ListNode(head.val)
            head = head.next
            cur1 = cur1.next
            count += 1

        while count <= right:
            cur2.next = ListNode(head.val)
            head = head.next
            cur2 = cur2.next
            count += 1
        
        while head:
            cur3.next = ListNode(head.val)
            head = head.next
            cur3 = cur3.next
        
        dummy2 = self.reverseList(dummy2.next)

        cur2 = dummy2

        while cur2.next:
            cur2 = cur2.next
        
        cur2.next = dummy3.next 
        cur1.next = dummy2

        return dummy1.next