# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pattern_count = Counter(pattern)
        ans = []

        def convertToNum(word):
            n = len(word)
            convertedWord = []
            i = 0

            while i < n:
                count = 1
                i += 1

                while i < n and word[i] == word[i - 1]:
                    i += 1
                    count += 1
                
                convertedWord.append(count)
            
            return convertedWord

        for word in words:
            word_count = Counter(word)
            flag = True

            for i in range(len(word)):
                if word_count[word[i]] != pattern_count[pattern[i]]:
                    flag = False

            if flag and convertToNum(word) == convertToNum(pattern):
                ans.append(word)

        return ans