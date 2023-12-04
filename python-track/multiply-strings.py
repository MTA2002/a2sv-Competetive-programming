class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_int=0
        num2_int=0
        for i in num1:
            num1_int=num1_int*10+int(i)
        for i in num2:
            num2_int=num2_int*10+int(i)
        return f"{num1_int*num2_int}"