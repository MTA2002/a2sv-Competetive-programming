class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        total = 0
        for cost in costs:
            total += cost
            if total > coins:
                break
            count += 1
        return count