class Solution:
    def maxScore(self, s: str) -> int:
        one_count = s.count('1')

        max_ = 0

        for i in range(len(s)-1):

            if s[i] == '1':
                one_count -= 1
                max_ = max(max_,one_count)

            else:
                one_count += 1
                max_ = max(max_,one_count)




        return max_