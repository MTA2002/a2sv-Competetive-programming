class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_length = 1
        count = 0
        size = len(answerKey)
        # maximizing true
        start = 0

        for i in range(size):
            if answerKey[i] == 'F':
                count += 1

            while count > k:
                if answerKey[start] == 'F':
                    count -= 1
                start += 1
            
            max_length = max(max_length,i-start+1)
        
        # maximizing false
        start = 0
        count = 0
        for i in range(size):
            if answerKey[i] == 'T':
                count += 1


            while count > k:
                if answerKey[start] == 'T':
                    count -= 1
                start += 1
            
            max_length = max(max_length,i-start+1)


        return max_length
