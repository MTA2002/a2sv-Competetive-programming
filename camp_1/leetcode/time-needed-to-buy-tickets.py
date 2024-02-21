class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_taken = 0
        i = 0

        while tickets[k] > 0:
            if tickets[i % len(tickets)] > 0:
                time_taken += 1
                tickets[i % len(tickets)] -= 1
            i += 1
        
        return time_taken

