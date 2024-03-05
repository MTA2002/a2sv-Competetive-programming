# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = defaultdict(list)
        max_ = 0

        def inorder(cur,level,idx):
            if cur:
                inorder(cur.left,level+1,2*idx)
                ans[level].append((cur.val,idx))
                inorder(cur.right,level+1,2*idx+1)
            

        inorder(root,0,0)

        for level,value in ans.items():
            max_ = max(max_,value[-1][1] - value[0][1] + 1)

        return max_