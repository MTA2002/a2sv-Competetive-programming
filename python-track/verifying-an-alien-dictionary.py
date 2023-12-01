class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        size=len(words)
        for i in range(size-1):
            j=0
            k=0
            while j<len(words[i]) and j<len(words[i+1]):
                if order.index(words[i][j])>order.index(words[i+1][j]):
                    return False
                elif order.index(words[i][j])<order.index(words[i+1][j]):
                    break
                j+=1
            if j==len(words[i]) or j==len(words[i+1]):
                j-=1
            if order.index(words[i][j])==order.index(words[i+1][j]):
                if len(words[i])>len(words[i+1]):
                    return False
        return True