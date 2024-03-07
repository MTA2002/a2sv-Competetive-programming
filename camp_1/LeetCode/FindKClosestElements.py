class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = []

        for a in arr:
            ans.append((abs(a - x),a))
        
        ans.sort()
        ans = [a for d,a in ans]
        ans = ans[:k]

        return sorted(ans)