class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_ = float('inf')
        left = 0
        count = 0

        for right in range(len(blocks)):
            if blocks[right] == 'W':
                count += 1

            if right - left + 1 == k:
                min_ = min(count,min_)
                if blocks[left] == 'W':
                    count -= 1
                left += 1
        
        return min_

                