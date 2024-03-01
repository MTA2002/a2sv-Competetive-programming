class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        adjacents = []

        for i in range(len(weights) - 1):
            adjacents.append(weights[i] + weights[i+1])
        
        adjacents.sort()
        max_ = sum(adjacents[:-k:-1])
        min_ = sum(adjacents[:k-1])

        return max_ - min_