# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = [Counter() for i in range(8)]
        ans = 0

        for ch, count in sorted(Counter(word).items(), reverse = True, key= lambda x:x[1]):
            
            for j in range(1, 4 + 1):
                flag = False
                for i in range(8):
                    if ch not in counter[i] and len(counter[i]) < j:
                        counter[i][ch] = j
                        ans += j * count
                        flag = True
                        break
                if flag:
                    break
        
        return ans