# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        global max_sum
        max_sum = 0

        def solve(cur: Optional[TreeNode]):
            global max_sum
            if cur:
                left_max,left_sum,left_min = solve(cur.left)
                right_max,right_sum,right_min = solve(cur.right)

                if cur.val > left_max and cur.val < right_min:
                    max_sum = max(max_sum,cur.val+left_sum+right_sum)
                    return (max(right_max,cur.val),left_sum+right_sum+cur.val,min(left_min,cur.val))
                
                return [float('inf'),0,float('-inf')]
            
            return [float('-inf'),0,float('inf')]

        solve(root)

        return max_sum
