class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:        
        agesSort = []
        for i in range(len(ages)):
            agesSort.append((ages[i], scores[i]))
        
        agesSort.sort()
        
        dp = [0 for i in range(len(ages))]
        
        for i in range(len(ages)):
            if i == 0:
                dp[i] = agesSort[i][1]
                continue
            
            curScore = agesSort[i][1]
            j = i-1
            choosen = 0
            while j >=0:
                if agesSort[j][1] <= curScore or agesSort[j][0] == agesSort[i][0]:
                    choosen = max(choosen, dp[j])
                j -= 1
            
            dp[i] = curScore + choosen
        
        return max(dp)