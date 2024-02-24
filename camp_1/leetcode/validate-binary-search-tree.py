# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []

        def inorder(cur :  Optional[TreeNode]):
            if cur:
                inorder(cur.left)
                ans.append(cur.val)
                inorder(cur.right)
        
        inorder(root)

        for i in range(1,len(ans)):
            if ans[i] <= ans[i-1]:
                return False
                
        return True
