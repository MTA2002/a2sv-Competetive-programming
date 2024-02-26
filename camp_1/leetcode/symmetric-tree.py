# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ans1 = []

        def inorder(current:Optional[TreeNode],isLeft:bool):
            if current:
                inorder(current.left,True)
                ans1.append((current.val,isLeft))
                inorder(current.right,False)
        
        ans2 = []
        def inorder2(current:Optional[TreeNode],isRight:bool):
            if current:
                inorder2(current.right,True)
                ans2.append((current.val,isRight))
                inorder2(current.left,False)

        inorder(root.left,True)
        inorder2(root.right,True)

        return ans1 == ans2

