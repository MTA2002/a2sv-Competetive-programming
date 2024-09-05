# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = []

        for ch in s:
            nums.append(str(ord(ch) - 96))

        nums = ''.join(nums)

        for _ in range(k):
            nums = str(sum([int(ch) for ch in nums]))

        return int(nums)