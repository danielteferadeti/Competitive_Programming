class Solution:
    def firstBadVersion(self, n: int) -> int:
        left_ver = 1
        right_ver = n
        last_bad = 1 
        
        while left_ver <= right_ver:
            mid_ver = (left_ver + right_ver)//2
            
            if isBadVersion(mid_ver):
                last_bad = mid_ver
                right_ver = mid_ver - 1
            else:
                left_ver = mid_ver + 1
        
        return last_bad