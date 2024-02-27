# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isSym(current1:Optional[TreeNode],current2:Optional[TreeNode]):
            if current1 and current2:

                return current1.val == current2.val and isSym(current1.left,current2.right) and isSym(current1.right,current2.left)
            
            if (current1 and not current2) or (not current1 and current2):
                return False

            if not current1 and not current2:
                return True


        return isSym(root.left,root.right)

