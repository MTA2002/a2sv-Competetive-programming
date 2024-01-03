class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        size = len(people)
        left = 0
        right = size - 1
        count = 0

        while left < right:
            if people[left] + people[right] <=limit:
                count += 1
                left += 1
            right -= 1

        return size - count

 