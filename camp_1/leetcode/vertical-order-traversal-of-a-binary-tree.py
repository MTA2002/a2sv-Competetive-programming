# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)

        def inorder(cur,row,col):
            if cur:
                ans[col].append((row,cur.val))
                inorder(cur.left,row+1,col-1,)
                inorder(cur.right,row+1,col+1)

        inorder(root,0,0)
        
        res = []

        for key,value in sorted(ans.items()):
            res.append([val for row,val in sorted(value)])
        
        return res
        