class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for ch in s:

            if ch == ']':
                num = 0
                word = []
                print(stack)
                while stack[-1] != '[':
                    poped = stack.pop()
                    if poped.isalpha():
                        word.append(poped)
                        
                stack.pop()
                num = []

                while stack and stack[-1].isnumeric():
                    num.append(stack.pop())

                num.reverse()  
                word.reverse()

                stack.append(''.join(word) * int(''.join(num)))
                print(word,stack)
            else:
                stack.append(ch)
        

        return "".join(stack)