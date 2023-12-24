class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        size = len(flips)
        binary_string = [1] * size

        for i in range(1,size):
            binary_string[i] = i+1 + binary_string[i-1]

        sum_of_flips = 0
        count = 0

        for idx,flip in enumerate(flips):
            sum_of_flips += flip
            if sum_of_flips == binary_string[idx]:
                count += 1
            
        return count
            

