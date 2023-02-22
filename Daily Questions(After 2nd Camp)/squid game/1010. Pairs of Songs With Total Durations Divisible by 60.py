class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mod_count = defaultdict(int)
        pair_count = 0
        
        for num in time:
            mod_count[num%60] += 1
        
        for mod in range(1, 30):
             pair_count += mod_count[mod] * mod_count[60-mod]
        
        n = mod_count[30]
        pair_count += n*(n-1) // 2
        
        n = mod_count[0]
        pair_count += n*(n-1) // 2
            
        return pair_count