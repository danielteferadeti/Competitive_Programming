class Solution:
    def minimumDeletions(self, s: str) -> int:
        bCount = []
        total = 0
        for char in s:
            if char == 'b':
                total += 1
            bCount.append(total)

        memo = {}
        def dp(idx):
            if idx in memo:
                return memo[idx]

            if idx == 0: return 0

            opt1, opt2 = 10**10, 10**10
            if s[idx] == 'a':
                opt1 = min(bCount[idx], dp(idx-1)+1)
            else:
                opt2 =  dp(idx-1)
            
            memo[idx] = min(opt1,opt2)
            return memo[idx]

        return dp(len(s)-1)