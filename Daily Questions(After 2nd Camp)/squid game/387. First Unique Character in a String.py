class Solution:
    def firstUniqChar(self, s: str) -> int:
        _dict = {}
        
        for i in range(len(s)):
            if s[i] in _dict: 
                indx, cnt = _dict[s[i]]
                _dict[s[i]] = (i, cnt+1)
            else: _dict[s[i]] = (i, 1)
        
        ind = sys.maxsize
        is_set = False
        for char in _dict:
            indx, count = _dict[char]
            if count ==1 and indx < ind: 
                ind = indx
                is_set = True
        
        return ind if is_set else -1