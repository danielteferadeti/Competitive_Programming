class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        if len(s) > 12: return []
        
        result = []
        
        def backTrack(idx, dots, sofar):
            if idx == len(s) and dots == 4:
                result.append(sofar[:-1])
                return
            
            if dots > 4: return
            
            for i in range(idx, min(idx+3, len(s))):
                if int(s[idx:i+1]) <= 255 and (i==idx or s[idx] != "0"):
                    backTrack(i+1, dots+1, sofar+s[idx:i+1] + ".")
            
        backTrack(0, 0, "")
        return result