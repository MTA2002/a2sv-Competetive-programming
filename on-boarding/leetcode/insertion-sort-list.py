# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        def insert(val):
            cur = dummy

            while cur.next and cur.next.val < val:
                cur = cur.next
            
            temp = ListNode(val)
            temp.next = cur.next
            cur.next = temp
        
        while head:
            insert(head.val)
            head = head.next

        return dummy.next