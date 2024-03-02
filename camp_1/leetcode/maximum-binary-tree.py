# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def solve(nums):
            if len(nums) == 0:
                return
            
            max_ = max(nums)
            index = nums.index(max_)

            return TreeNode(max_,solve(nums[:index]),solve(nums[index+1:]))
        
        return solve(nums)
