class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix_sum = [0] * 1001

        for numPassenger,from_,to in trips:
            prefix_sum[from_] += numPassenger
            prefix_sum[to] -= numPassenger

        sum_ = 0

        for val in prefix_sum:
            sum_ += val
            if sum_ > capacity:
                return False

        return True


