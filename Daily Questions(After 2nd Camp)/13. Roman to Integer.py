class Solution:
    def romanToInt(self, s: str) -> int:
        _dict = {"I": 1, "V":5, "X":10, "L":50, "C": 100, "D": 500, "M":1000 }
        
        cur = len(s)-1
        result = 0
        while cur >=0:
            if cur==0 or _dict[s[cur]] <= _dict[s[cur-1]]:
                result += _dict[s[cur]]
                cur -=1
            else:
                result += _dict[s[cur]] - _dict[s[cur-1]]
                cur-=2
        
        return result