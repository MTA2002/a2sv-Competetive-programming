class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()
        left = 0
        max_ = float('-inf')

        for right in range(len(s)):
            counter[s[right]] += 1  

            while (right - left + 1) - counter[max(counter,key=counter.get)] > k:
                counter[s[left]] -= 1
                left += 1
            
            max_ = max(max_,right - left + 1)
        
        return max_