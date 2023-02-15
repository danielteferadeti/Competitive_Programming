class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber > 26:
            q = columnNumber//26
            r = columnNumber%26
            
            if r:
                ans.append(chr(64+r)) 
            else:
                ans.append(chr(64+26))
                q -= 1
            columnNumber = q
        
        if columnNumber: ans.append(chr(64+columnNumber))
        
        return "".join(ans[::-1])