class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        total = 1
        original = capacity
        capacity -= plants[0]
        
        for i in range(1,len(plants)):
            waterNeeded = plants[i]
            
            if waterNeeded <= capacity:
                total += 1
                capacity -= waterNeeded
            else:
                total += (((i+1)*2)-1)
                capacity = original
                capacity -= waterNeeded
        return total