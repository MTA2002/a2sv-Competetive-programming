class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        my_set=set()
        for range_value in ranges:
            for r in range(range_value[0],range_value[1]+1):
                my_set.add(r)

        for i in range(left,right+1):
          if i not in my_set:
            return False
        return True
    