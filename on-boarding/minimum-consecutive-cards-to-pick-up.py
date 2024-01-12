class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        min_ = float('inf')
        left = 0
        cards_count = Counter()

        for right in range(len(cards)):
            cards_count[cards[right]] += 1

            while cards_count[cards[right]] > 1:
                min_ = min(min_,right - left + 1)
                cards_count[cards[left]] -= 1
                left += 1
            
        return min_ if min_ != float('inf') else -1
