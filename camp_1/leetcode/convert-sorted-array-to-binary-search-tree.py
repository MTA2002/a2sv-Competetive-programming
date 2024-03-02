# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def solve(nums):
            if len(nums) == 0:
                return
            
            mid = len(nums) // 2
            

            return TreeNode(nums[mid],solve(nums[:mid]),solve(nums[mid+1:]))
        
        return solve(nums)