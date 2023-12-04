class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        mine=abs(target[0])+abs(target[1])
        for ghost in ghosts:
            total=abs(ghost[0]-target[0])+abs(ghost[1]-target[1])
            if total<=mine:
                return False
        return True