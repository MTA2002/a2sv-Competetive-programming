class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        string_to_list=[]
        j=0
        for index,letter in enumerate(s):
          if j<len(spaces) and index==spaces[j]:
            string_to_list.append(" "+letter)
            j+=1
          else:
            string_to_list.append(letter)
        return ''.join(string_to_list)