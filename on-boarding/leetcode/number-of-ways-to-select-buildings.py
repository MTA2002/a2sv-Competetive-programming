class Solution:
    def numberOfWays(self, s: str) -> int:
        length = len(s)
        zero_count = 0
        zero_one_count_arr = []
        one_count = 0
        one_zero_count_arr = []

        for i in range(length):
            if s[i] == '0':
                zero_count += 1
                one_zero_count_arr.append(one_count)
                zero_one_count_arr.append(0)
            else:
                one_count += 1
                zero_one_count_arr.append(zero_count)
                one_zero_count_arr.append(0)
        
        for i in range(1,length):
            zero_one_count_arr[i] += zero_one_count_arr[i-1]
            one_zero_count_arr[i] += one_zero_count_arr[i-1]
        
        ans = 0

        for i in range(length):
            if s[i] == '0':
                ans += zero_one_count_arr[i]
            else:
                ans += one_zero_count_arr[i]


        return ans

        