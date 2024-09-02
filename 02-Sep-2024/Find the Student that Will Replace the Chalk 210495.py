# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        rem = k % sum(chalk)
        prev = 0

        for idx, c in enumerate(chalk):
            if prev <= rem < prev + c:
                return idx

            prev += c

        return 0