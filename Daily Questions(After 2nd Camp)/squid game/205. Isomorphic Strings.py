class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        _dict = {}
        preserved = set()
        
        for i in range(len(s)):
            if s[i] not in _dict and t[i] not in preserved:
                _dict[s[i]] = t[i]
                preserved.add(t[i])
            elif s[i] in _dict:
                if _dict[s[i]] == t[i]:
                    pass
                else:
                    return False
            else:
                return False

        return True