# Problem: Linked List in Binary Tree - https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        @cache
        def traverse(cur_node, curHead):
            if not curHead:
                return True

            if cur_node:
                left_ans , right_ans = 0, 0
                if cur_node.val == curHead.val:
                    left_ans = traverse(cur_node.left, curHead.next)
                    right_ans = traverse(cur_node.right, curHead.next)

                    if left_ans or right_ans:
                        return True

                left_ans = traverse(cur_node.left, head)
                right_ans = traverse(cur_node.right, head)

                if left_ans or right_ans:
                    return True
        
        return traverse(root, head)