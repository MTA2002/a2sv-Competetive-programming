# Problem: Process Restricted Friend Requests - https://leetcode.com/problems/process-restricted-friend-requests/

class DSU:
    def __init__(self, n):
        self.parents = {i:i for i in range(n)}
        self.size = defaultdict(lambda: 1)
    
    def find(self, x):

        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        
        return x
    
    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        self.parents[parentY] = parentX
        
    
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)
    
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        dsu = DSU(n)
        ans = []

        for u, v in requests:
            copy = dsu.parents.copy()
            dsu.union(u, v)

            for x, y in restrictions:
                if dsu.isConnected(x, y):
                    ans.append(False)
                    dsu.parents = copy
                    break
            else:
                ans.append(True)

        return ans