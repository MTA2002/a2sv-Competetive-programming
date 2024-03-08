class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        counter = Counter()
        self.times_ = []
        max_ = float('-inf')
        p = 0
        for i,person in enumerate(persons):
            counter[person] += 1
            if counter[person] >= max_:
                max_ = counter[person]
                p = person
            self.times_.append((times[i],p))

    def q(self, t: int) -> int:
        low , high = 0 , len(self.times_) - 1
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2

            if self.times_[mid][0] <= t:
                ans = self.times_[mid]
                low = mid + 1
            else:
                high = mid - 1

        return ans[1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)