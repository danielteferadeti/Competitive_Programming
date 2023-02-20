class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIPV6(q):
            v6 = q.split(":")
            if len(v6) != 8: return False
            _set = {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}
            
            for char in v6:
                if not char or len(char)> 4: return False
                for c in char:
                    if not c.isdigit(): c = c.lower()
                    if c not in _set: return False
            
            return True
        
        def isIpv4(q):
            v4 = q.split(".")
            if len(v4) != 4: return False
            
            for char in v4:
                if not char.isdigit(): return False
                if (char and char[0] == "0" and len(char)!=1) or int(char) > 255: return False
                            
            return True
        
        
        if isIpv4(queryIP): return "IPv4"
        if isIPV6(queryIP): return "IPv6"
        
        return "Neither"
        
        
        