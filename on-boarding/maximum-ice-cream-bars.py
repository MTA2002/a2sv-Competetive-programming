class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_ = max(costs)
        sorted_list = [0 for i in range(max_)]
        count = 0
        total = 0

        for cost in costs:
            sorted_list[cost - 1] += 1
            
        costs = []
        for idx,element in enumerate(sorted_list):
            costs.extend([idx+1]*element)

        for cost in costs:
            total += cost
            if total > coins:
                break
            count += 1
            


        return count
