# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_ = []

        while head:
            list_.append(head.val)
            head = head.next

        list_c = list_.copy()
        list_.reverse()
        return list_c == list_ 