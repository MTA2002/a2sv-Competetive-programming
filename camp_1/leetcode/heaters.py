class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        heaters_size = len(heaters)
        heaters.sort()

        def helper(radius):

            for house in houses:
                pos = bisect_left(heaters, house)

                if pos == heaters_size:
                    pos = heaters_size - 1

                option1 = abs(heaters[pos] - house) <= radius
                option2 = abs(heaters[pos - 1] - house) <= radius if pos - 1 >= 0 else False
                option3 = abs(heaters[pos + 1] - house) <= radius if pos + 1 < heaters_size else False

                if not option1 and not option2 and not option3:
                    return False
            
            return True
        
        low ,  high = 0 , 10 ** 9
        ans = 10 ** 9

        while low <= high:
            mid = (low + high) // 2

            if helper(mid):
                ans = min(ans,mid)
                high = mid - 1
            else:
                low = mid + 1

        return ans

