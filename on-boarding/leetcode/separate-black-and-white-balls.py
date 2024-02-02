class Solution:
    def minimumSteps(self, s: str) -> int:
        black_count = 0
        ans = 0

        for color in s:
            if color == '1':
                black_count += 1
            else:
                ans += black_count
        
        return ans