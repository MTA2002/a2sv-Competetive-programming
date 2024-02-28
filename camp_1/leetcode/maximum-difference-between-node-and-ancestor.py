# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        global max_
        max_ = 0

        def inorder(cur: Optional[TreeNode]):
            global max_
            if cur:
                left_ans = inorder(cur.left)
                right_ans = inorder(cur.right)
                new_ans = [100001,-1]
                
                new_ans[0] = min(left_ans[0],right_ans[0],cur.val)
                new_ans[1] = max(left_ans[1],right_ans[1],cur.val)
                max_ = max(max_,abs(cur.val - new_ans[0]),abs(cur.val - new_ans[1]))
                
                return new_ans

            return [100001,-1]
        
        inorder(root)
        

        return max_