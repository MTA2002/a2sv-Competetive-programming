class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled_array=[]

        for i in range(n):
            shuffled_array.append(nums[i])
            shuffled_array.append(nums[i+n])
            
        return shuffled_array
