# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return sorted(nums, key = lambda x: int("".join([str(mapping[int(ch)]) for ch in str(x)])))