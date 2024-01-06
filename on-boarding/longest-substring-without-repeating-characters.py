class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        s_count = Counter()
        max_ = 0

        for right in range(len(s)):
            s_count[s[right]] += 1

            while s_count[s[right]] > 1:
                s_count[s[left]] -= 1
                left += 1
            max_ = max(max_,right-left+1)
        
        return max_


        