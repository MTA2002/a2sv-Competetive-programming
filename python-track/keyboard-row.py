class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row="qwertyuiop"
        second_row="asdfghjkl"
        third_row="zxcvbnm"
        ans=[]
        for word in words:
            row=1
            condition=True
            if word[0].lower() in second_row:
                row=2
            elif word[0].lower() in third_row:
                row=3
            for letter in word:
                if row==1 and letter.lower() not in first_row:
                    condition=False
                    break
                elif row==2 and letter.lower() not in second_row:
                    condition=False
                    break
                elif row==3 and letter.lower() not in third_row:
                    condition=False
                    break
            if condition:
                ans.append(word)

        return ans