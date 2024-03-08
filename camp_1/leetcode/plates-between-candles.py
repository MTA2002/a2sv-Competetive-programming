class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        plate_count = 0
        prefix_sum = []
        candles = []

        for i,ch in enumerate(s):
            if ch == '*':
                plate_count += 1
            else:
                candles.append(i)
            prefix_sum.append(plate_count)

        ans = []

        for query in queries:
            left = bisect_left(candles,query[0])
            right = bisect_left(candles,query[1])
            
            if right == len(candles):
                right -= 1
            elif query[1] != candles[right]:
                right -= 1

            val = 0
            if right > left: 
                val += prefix_sum[candles[right]]
                val -= prefix_sum[candles[left] - 1] if candles[left] - 1 >= 0 else 0

            ans.append(val)


        return ans