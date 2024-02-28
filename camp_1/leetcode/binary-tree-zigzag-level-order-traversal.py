# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)

        def inorder(cur,level):
            if cur:
                inorder(cur.left,level+1)
                ans[level].append(cur.val)
                inorder(cur.right,level+1)

        inorder(root,0)

        res = []

        for key,value in sorted(ans.items()):
            if key % 2 == 0:
                res.append(value)
            else:
                res.append(value[::-1])

        return res
        