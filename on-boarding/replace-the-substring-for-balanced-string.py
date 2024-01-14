class Solution:
    def balancedString(self, s: str) -> int:
        letters = {'Q', 'W', 'E', 'R'}

        def contains(counter1:Counter , counter2:Counter):
            for key in counter1:
                if counter2[key] <  counter1[key]:
                    return False
            return True

        s_count = Counter(s)
        target = len(s) // 4
        target_count = Counter()

        for letter in letters:
            diff = s_count[letter] - target
            if diff > 0:
                target_count[letter] += diff

        current_count = Counter()
        left = 0
        min_ = float('inf')
        
        if len(target_count) == 0:
            return 0
            
        for right in range(len(s)):
            current_count[s[right]] += 1
            
            while contains(target_count,current_count):
                min_ = min(min_,right-left+1)
                current_count[s[left]] -= 1
                left += 1
        
        return min_
