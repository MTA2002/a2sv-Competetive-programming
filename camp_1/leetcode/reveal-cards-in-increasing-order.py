class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        ans = deque()

        for i in range(len(deck)):

            if ans:
                ans.appendleft(ans.pop())
            
            ans.appendleft(deck[i])
        
        return ans