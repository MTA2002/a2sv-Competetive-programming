class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        count = 0

        for key in counter:
            count += counter[key] if counter[key] % (key + 1) == 0 else (counter[key] // (key + 1))  * (key + 1) + (key + 1)
            


        return count