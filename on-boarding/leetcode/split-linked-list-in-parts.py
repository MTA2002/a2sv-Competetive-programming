# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        cur = head

        while cur:
            cur = cur.next
            count += 1
        
        mod_count = 0
        cur = head
        ans = []
        
        for i in range(k):
            c = count // k
            prev = ListNode()
            if mod_count < count % k:
                mod_count += 1
                c += 1
            
            ans.append(cur)
            
            while c and cur:
                c -= 1
                prev = cur
                cur = cur.next

            prev.next = None
            

        return ans


        
        