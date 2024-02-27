class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def solve(left,right,turn):

            if left > right:
                return 0

            choice1 = nums[left] if turn else -nums[left] 
            choice2 = nums[right] if turn else -nums[right] 

            if turn:
                return max((choice1 + solve(left+1, right,not turn)),(choice2 + solve(left, right - 1,not turn)))
            else:
                return min((choice1 + solve(left+1, right,not turn)),(choice2 + solve(left, right - 1,not turn)))

        
        return solve(0,len(nums)-1,True) >= 0