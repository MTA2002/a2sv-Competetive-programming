class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        row_size=len(strs)
        col_size=len(strs[0])
        count=0
        
        for col in range(col_size):
            word=[]
            for row in range(row_size):
                word.append(strs[row][col])
            if sorted(word)!=word:
                count += 1
            


        return count
