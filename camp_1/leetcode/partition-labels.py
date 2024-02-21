class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dict_ = {}
        size = len(s)

        for i in range(size):
            dict_[s[i]] = i

        ans = []
        max_ = 0
        sum_ = 0

        for i in range(size):
            index = dict_[s[i]]
            max_ = max(max_,index)

            if i == max_:
                ans.append(i+1 - sum_)
                sum_ = i+1
        
        return ans
                                                                                         