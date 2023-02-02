class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:      
        digits = []
        letters = []
        
        for i in range(len(logs)):
            j = 0
            log = logs[i]
            while log[j] != " ":
                j += 1
            
            firstChar = log[j+1]
            isDigit = firstChar.isnumeric()
            if isDigit: digits.append(log)
            else:
                newOrd = log[j+1: ]
                letters.append((newOrd, log[:j], i))
        letters.sort()
        
        ans = []
        
        for let in letters:
            ans.append(logs[let[2]])
        
        ans += digits
        return ans