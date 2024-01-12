class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0 
        fruits_basket = Counter()
        max_ = float('-inf')

        for right in range(len(fruits)):
            fruits_basket[fruits[right]] += 1

            while len(fruits_basket) > 2:
                fruits_basket[fruits[left]] -= 1
                if fruits_basket[fruits[left]] == 0:
                    del fruits_basket[fruits[left]]
                left += 1
            max_ = max(max_,right-left+1)

        return max_
