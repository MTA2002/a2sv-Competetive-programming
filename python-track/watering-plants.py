class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        total_capcity=capacity
        number_of_steps=0
        for i,plant in enumerate(plants):
            if capacity>=plant:
                number_of_steps+=1
            else:
                capacity=total_capcity
                number_of_steps+=i
                number_of_steps+=i+1
            capacity-=plant
        return number_of_steps