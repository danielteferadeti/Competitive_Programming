class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def reverser(strn):
            strr = ""
            for i in strn:
                strr = i + strr
            return strr
        
        def isPal(strn):
            if strn == reverser(strn):
                return True
            return False
        
        l,r = 0, len(s)-1
        while l < r:
            if s[l]==s[r]:
                l +=1
                r -=1
            else:
                check_right = isPal(s[l+1:r+1])
                check_left = isPal(s[l:r])
                if check_right: return check_right
                else: return check_left
        return True