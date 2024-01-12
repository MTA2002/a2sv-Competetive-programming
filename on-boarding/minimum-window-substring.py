class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def contains(counter1:Counter , counter2:Counter):
            for key in counter1:
                if counter2[key] <  counter1[key]:
                    return False
            return True

        t_count = Counter(t)
        s_count = Counter()
        left = 0
        min_ = float('inf')
        firstIdx = 0
        lastIdx = 0
        for right in range(len(s)):
            s_count[s[right]] += 1
            
            while contains(t_count,s_count):
                if right - left + 1 < min_:
                    min_ = right - left + 1
                    firstIdx = left
                    lastIdx = right
                s_count[s[left]] -= 1
                left += 1

        if min_ == float('inf'):
            return ""

        return s[firstIdx:lastIdx+1]
        