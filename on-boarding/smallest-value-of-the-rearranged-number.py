class Solution:
    def smallestNumber(self, num: int) -> int:
        
        if num > 0:

            num_list = list(str(num))
            size = len(num_list)
            for i in range(size):
                for j in range(size-i-1):
                    order1 = int(num_list[j] + num_list[j+1])
                    order2 = int(num_list[j+1] + num_list[j])
                    if order1 > order2:
                        num_list[j] , num_list[j+1] = num_list[j+1] , num_list[j]

            if num_list[0] == '0':
                for i in range(size):
                    if num_list[i] != '0':
                        num_list[i] , num_list[0] = num_list[0] , num_list[i]
                        break

            return int(''.join(num_list))

        elif num < 0:

            num *= -1
            num_list = list(str(num))
            size = len(num_list)
            for i in range(size):
                for j in range(size-i-1):
                    order1 = int(num_list[j] + num_list[j+1])
                    order2 = int(num_list[j+1] + num_list[j])
                    if order2 > order1:
                        num_list[j] , num_list[j+1] = num_list[j+1] , num_list[j]

            return -int(''.join(num_list))

        return num