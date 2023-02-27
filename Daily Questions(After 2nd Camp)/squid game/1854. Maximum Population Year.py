class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        max_pop = -1 * 10**10
        ans_year = 1950
        
        for year in range(1950, 2051):
            count = 0
            for birth, death in logs:
                if birth <= year < death:
                    count += 1
            if count > max_pop:
                max_pop = count
                ans_year = year
        
        return ans_year