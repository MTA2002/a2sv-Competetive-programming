# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        size = len(arr)

        for i in range(1,size):
            arr[i] ^= arr[i-1]

        ans = []
        for left,right in queries:
            res = arr[right]

            if left - 1 >= 0:
                res ^= arr[left-1]
            
            ans.append(res)
    
        return ans

