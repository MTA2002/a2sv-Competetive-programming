class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        left = 0
        right = 0

        if len(name) > len(typed):
            return False
        
        while left < len(name) and right < len(typed):
            left1 = left
            if typed[right] != name[left]:
                return False

            while left1 < len(name):
                if name[left1] != name[left]:
                    break
                left1 += 1

            right1 = right

            while right1 < len(typed):
                if typed[right1] != typed[right]:
                    break
                right1 += 1

            if right1 - right < left1 - left:
                return False

            left = left1
            right = right1
            
        if left < len(name):
            return False

        for r in range(right,len(typed)):
            if typed[r] != name[-1]:
                return False

            
         

        return True

            