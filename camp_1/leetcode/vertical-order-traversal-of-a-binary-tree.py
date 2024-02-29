# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from sortedcontainers import SortedList 

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)

        def inorder(cur,row,col):
            if cur:
                ans[col].append((cur.val,row))
                inorder(cur.left,row+1,col-1,)
                inorder(cur.right,row+1,col+1)

        inorder(root,0,0)
        
        res = []

        for key,value in sorted(ans.items()):
            value.sort(key = lambda x:(x[1],x[0]))
            temp = []
            for val in value:
                temp.append(val[0])
            res.append(temp)
        
        return res
        
