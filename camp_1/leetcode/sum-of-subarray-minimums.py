class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = [1]*len(arr)
        arr.append(-1)
        stack = [(float('-inf'),-1)]

        for i in range(len(arr)):

            while stack[-1][0] > arr[i]:
                ans[stack[-1][1]] *= i - stack[-1][1]
                stack.pop()

            if i < len(arr) - 1:
                ans[i] *= i - stack[-1][1]

            stack.append((arr[i],i))


        for i in range(len(arr)-1):
            ans[i] *= arr[i]

        return sum(ans) % (10 ** 9 + 7)