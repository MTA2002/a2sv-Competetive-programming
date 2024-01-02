class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = []

        for letter in s:
            if letter.isalnum():
                if letter.isupper():
                    word.append(letter.lower())
                else:
                    word.append(letter)
        reverse = word.copy()
        word.reverse()   
        return word == reverse