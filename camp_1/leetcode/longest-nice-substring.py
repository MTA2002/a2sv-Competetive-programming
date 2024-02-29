class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        longest = 0
        ans = [-1,-1]
        size = len(s)

        def isNice(word):
            set_ = set(word)

            for letter in word:
                if letter.upper() not in set_ or letter.lower() not in set_:
                    return False

            return True 

        for i in range(size):
            for j in range(size):
                if isNice(s[i:j+1]) and j - i + 1 > longest:
                    longest = j - i + 1
                    ans[0] = i
                    ans[1] = j
        
        return s[ans[0]:ans[1]+1]
            
