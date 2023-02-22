class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        oprs = 0
        
        given = [_ for _ in s]
        
        for i in range(len(s)):
            counted = False
            new_s = [_ for _ in given]
            for j in range(1,len(s)):
                if given[j-1] == "0" and given[j] == "1":
                    new_s[j],  new_s[j-1] = new_s[j-1], new_s[j]
                    if not counted:
                        oprs += 1
                        counted = True
            
            given = [_ for _ in new_s]
        
        return oprs