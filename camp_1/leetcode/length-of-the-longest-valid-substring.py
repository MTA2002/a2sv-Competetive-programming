class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        n = len(word)
        forbidden = set(forbidden)
        quee = deque()
        max_ = -inf

        def check(arr):
            new_arr = []
            i = 0
            while quee and i >= -10:
                new_arr.append(arr.pop())
                i -= 1
            
            new_arr.reverse()
            for i in range(len(new_arr)):
                for j in range(i,len(new_arr)):
                    if "".join(new_arr[i:j+1]) in forbidden:
                        new_arr.reverse()
                        while new_arr:
                            arr.append(new_arr.pop())
                        return True
            new_arr.reverse()
            while new_arr:
                arr.append(new_arr.pop())

        
        for i in range(n):
            quee.append(word[i])
            
            while quee and check(quee):
                quee.popleft()
            
            # print(quee)
            max_ = max(max_,len(quee))

        return max_