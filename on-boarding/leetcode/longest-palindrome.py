class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest = 0
        counter = Counter(s)
        max_odd = 0
        
        for key in counter:

            if counter[key] % 2 == 0:
                longest += counter[key] 
            elif counter[key] > max_odd:
                longest += max_odd - 1 if max_odd else 0
                max_odd = counter[key]
            else:
                longest += counter[key] - 1

        return longest + max_odd