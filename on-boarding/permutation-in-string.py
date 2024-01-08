class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = Counter(s1)
        
        k = len(s1)
        left = 0

        for i in range(len(s2)):
            if i + 1 >= k:
                s2_dict = Counter(s2[left:i+1])
                if s2_dict == s1_dict:
                    return True
                left += 1

        return False