# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans1 = []
        ans2 = []

        def inorder(current:Optional[TreeNode],arr:List[int],isLeft:bool):
            if current:
                inorder(current.left,arr,True)
                arr.append((current.val,isLeft))
                inorder(current.right,arr,False)

        inorder(p,ans1,False)
        inorder(q,ans2,False)

        return ans1 == ans2



