class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        sortArray = [(-growTime[i],plantTime[i],i) for i in range(len(plantTime))]
        sortArray.sort()
        
        bestMax = 0
        platingDays = 0
        for i in range(len(sortArray)):
            platingDays += plantTime[sortArray[i][2]]
            bestMax = max(bestMax, platingDays+growTime[sortArray[i][2]])
            
        return bestMax