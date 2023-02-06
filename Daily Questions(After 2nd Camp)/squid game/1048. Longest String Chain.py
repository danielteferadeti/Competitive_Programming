class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        res = 1
        
        sortedByLen = []
        for idx, word in enumerate(words):
            sortedByLen.append((len(word), idx))
        sortedByLen.sort()
        
        sortedWords = []
        for leng, idx in sortedByLen:
            sortedWords.append(words[idx])
        
        for word in sortedWords:
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1 :]
                if prev in dp:
                    if dp[prev] + 1 > dp[word]:
                        dp[word] = dp[prev] + 1
                    res = max(res, dp[word])
                    
        return res