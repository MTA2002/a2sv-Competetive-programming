class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        left = 0
        max_count = float('-inf')
        count = 0
        
        for right in range(len(s)):
            if s[right] in vowels:
                count += 1

            if right - left + 1 == k:
                max_count = max(max_count,count)
                if s[left] in vowels:
                    count -= 1
                left += 1
        
        return max_count

