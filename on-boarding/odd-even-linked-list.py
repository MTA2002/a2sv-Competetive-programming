# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = ListNode()
        odd_current = odd_head

        even_head = ListNode()
        even_current = even_head

        temp = head

        idx = 1
        
        while temp:
            if idx % 2 == 0:
                even_current.next = ListNode(temp.val)
                even_current = even_current.next
            else:
                odd_current.next = ListNode(temp.val)
                odd_current = odd_current.next
            idx += 1
            temp = temp.next
        
        even_head = even_head.next
        odd_current.next = even_head

        return odd_head.next

        