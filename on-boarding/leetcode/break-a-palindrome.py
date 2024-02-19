class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome = list(palindrome)
        length = len(palindrome)

        if length == 1:
            return ""
        found = False

        for i in range(length):
            if palindrome[i] != 'a':
                if (length % 2 == 1 and i == length // 2) == False:
                    palindrome[i] = 'a'
                    found = True
                    break

        if found != True:
            palindrome[-1] = 'b'

        return "".join(palindrome)
        
