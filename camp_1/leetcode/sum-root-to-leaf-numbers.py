# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        global num 
        global ans 
        num = 0
        ans = 0

        def inorder(cur): 
            global num 
            global ans  

            if cur:
                num = 10 * num + cur.val
                inorder(cur.left)
                inorder(cur.right)
                if not cur.left and not cur.right:
                    ans += num
                
                num -= cur.val
                num //= 10

        inorder(root)

        return ans