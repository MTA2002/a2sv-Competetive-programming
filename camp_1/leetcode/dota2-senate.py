class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiants = deque()
        dires = deque()
        size = len(senate)
        check = [True] * size
        
        for i,s in enumerate(senate):
            if s == 'R':
                radiants.append((s,i))
            else:
                dires.append((s,i))
        
        i = 0
        
        while (radiants and dires):
            
            if senate[i%size] == 'R':
                if check[i%size] == True:
                    dire = dires.popleft()
                    check[dire[1]] = False 
                    radiants.append(radiants.popleft())
            else:
                if check[i%size] == True:
                    radiant = radiants.popleft() 
                    check[radiant[1]] = False
                    dires.append(dires.popleft()) 
            i += 1
        

        return "Radiant" if len(radiants) > len(dires) else "Dire"
