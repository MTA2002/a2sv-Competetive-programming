class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill) - 1
        target = skill[0] + skill[-1]
        total_chemistry = 0

        while left < right:
            if skill[left] + skill[right] != target:
                return -1
            else:
                total_chemistry += skill[left] * skill[right]
            left += 1
            right -= 1

        return total_chemistry

