class Solution:
    def reverseWords(self, s: str) -> str:
        separated_list=s.split()
        separated_list.reverse()
        return " ".join(separated_list)