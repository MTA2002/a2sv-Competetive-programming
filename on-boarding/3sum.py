class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        size = len(nums)
        nums_dict = {}

        for i in range(size):
            target = -1 * nums[i]
            for j in range(i+1,size):
                if target - nums[j] in nums_dict:
                    if j!= nums_dict[target - nums[j]] and nums_dict[target - nums[j]] != i:
                        ans.add(tuple(sorted([nums[i],nums[j],target - nums[j]])))
            nums_dict[nums[i]] = i

        res = []
        for element in ans:
            res.append(list(element))

        return res

