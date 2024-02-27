# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum_ = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def inorder(current:Optional[TreeNode]):
            if current:
                inorder(current.left)
                if current.val >= low and current.val <= high:
                    self.sum_ += current.val
                inorder(current.right)

        inorder(root)

        return self.sum_

