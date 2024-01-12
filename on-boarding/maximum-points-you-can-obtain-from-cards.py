class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        arr = []

        size = len(cardPoints)
        arr.extend(cardPoints[:k])
        arr.extend(cardPoints[size - k:])

        sum_ = sum(cardPoints[:k])
        max_sum = sum_

        right = len(arr) - 1
        left = k - 1
        print(arr)
        while right != k-1:
            sum_ += arr[right]
            sum_ -= arr[left]
            print(sum_)
            max_sum = max(sum_,max_sum)
            right -= 1
            left -= 1
            if left == -1:
                left = len(arr) - 1
        return max_sum
