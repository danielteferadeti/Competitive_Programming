class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
         
        def dp(given):
            dp = []
            n = len(given)
            for i in range(n):
                dp.append(defaultdict(int))

            for i in range(1,n):
                for j in range(i):
                    if given[i] >= given[j]:
                        dif = given[j] - given[i]
                        dp[i][dif] = dp[j][dif] + 1

            longest  = 0
            for _dicts in dp:
                for val in _dicts.values():
                        longest = max(longest, val)
            
            return longest + 1
            
            
        bestLongest = max(dp(nums), dp(nums[::-1]))            
        return bestLongest