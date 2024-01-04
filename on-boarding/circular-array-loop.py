class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        size = len(nums)

        for i in range(size):
            if nums[i]%size == 0:
                continue
            idx = (i + nums[i]) % size 
            for j in range(size):
                if nums[idx]/nums[i] < 0:
                    break

                idx = (idx + nums[idx]) % size 

                if idx == i:
                    return True

        return False