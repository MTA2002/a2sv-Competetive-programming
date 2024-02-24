# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.idx = 0
        self.ans = 1

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(current: Optional[TreeNode]):
            if current:
                inorder(current.left)
                self.idx += 1
                if self.idx == k:
                    self.ans = current.val
                inorder(current.right)
        
        inorder(root)

        return self.ans


