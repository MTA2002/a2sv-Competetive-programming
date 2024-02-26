# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        sum_ = []

        def inorder(cur):                
            if cur:
                ans.append(str(cur.val))
                inorder(cur.left)
                inorder(cur.right)
                if not cur.left and not cur.right:
                    sum_.append(int("".join(ans)))
                ans.pop()



        inorder(root)

        return sum(sum_)