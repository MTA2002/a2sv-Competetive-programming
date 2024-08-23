# Problem: Fraction Addition and Subtraction - https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution:
    def fractionAddition(self, expression: str) -> str:
        n = len(expression)
        numerator1, denominator1 = 0, 0
        i = 0

        if expression[0] == '-':
            i += 1
            while expression[i].isnumeric():
                numerator1 = numerator1 * 10 + int(expression[i])
                i += 1
            
            i += 1

            while i < n and expression[i].isnumeric():
                denominator1 = denominator1 * 10 + int(expression[i])
                i += 1

            numerator1 *= -1
        else:
            while expression[i].isnumeric():
                numerator1 = numerator1 * 10 + int(expression[i])
                i += 1
            
            i += 1

            while i < n and expression[i].isnumeric():
                denominator1 = denominator1 * 10 + int(expression[i])
                i += 1
        
        while i < n:
            sign = expression[i]
            i += 1
            numerator2 = 0
            denominator2 = 0

            while expression[i].isnumeric():
                numerator2 = numerator2 * 10 + int(expression[i])
                i += 1
            
            i += 1

            while i < n and expression[i].isnumeric():
                denominator2 = denominator2 * 10 + int(expression[i])
                i += 1
            
            print(sign, numerator2, denominator2)
            numerator1 *= denominator2
            numerator2 *= denominator1
            denominator1 *= denominator2

            if sign == '-':
                numerator1 -= numerator2
            else:
                numerator1 += numerator2
        
        gcd_ = gcd(numerator1, denominator1)

        numerator1 /= gcd_
        denominator1 /= gcd_

        return f'{int(numerator1)}/{int(denominator1)}'