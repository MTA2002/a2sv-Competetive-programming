class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low , high = 0 , len(letters) - 1
        smallestLetter = letters[0]

        while low <= high:
            mid = (low + high) // 2

            if letters[mid] > target:
                smallestLetter = letters[mid]
                high = mid - 1
            else:
                low = mid + 1
        
        return smallestLetter