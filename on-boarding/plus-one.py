class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number=0
        for idx,digit in enumerate(digits):
            number *= 10
            number += digit
        number += 1
        number = str(number)
        result=[int(num) for num in number]
        return result