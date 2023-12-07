class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners=set()
        losers={}

        for matche in matches:
            winners.add(matche[0])
            losers[matche[1]]=losers.get(matche[1],0)+1

        winners_list=[]
        losers_list=[]

        for winner in winners:
          if winner not in losers:
            winners_list.append(winner)

        for loser in losers:
          if losers[loser]==1:
            losers_list.append(loser)

        answer=[]
        answer.append(sorted(winners_list))
        answer.append(sorted(losers_list))

        return answer