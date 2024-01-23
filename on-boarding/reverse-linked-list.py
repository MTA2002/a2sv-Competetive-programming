# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer2 = head

        while pointer2 and pointer2.next:
            pointer2 = pointer2.next
        
        new_head = pointer2 if pointer2 else None

        while head and head.next:
            pointer1 = head

            while pointer1.next != pointer2:
                pointer1 = pointer1.next
            
            pointer2.next = pointer1
            pointer1.next = None
            pointer2 = pointer2.next
        
        return new_head
            


