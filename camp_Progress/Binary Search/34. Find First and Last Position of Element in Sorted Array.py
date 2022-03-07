class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        first_targ = -1
        last_targ = -1
        
        l = 0
        r = len(nums) -1
        while l <= r:
            m = (l + r)//2
            
            if nums[m] == target:
                first_targ = m
                last_targ = m
                break 
            elif nums[m] < target:
                l = m + 1
            else:
                r = m -1
        
        if first_targ == -1:
             return [-1,-1]
        #Left side
        l = 0
        r = first_targ
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                first_targ = m
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
                
        #Right Side 
        l = last_targ
        r = len(nums) -1
        while l <= r:
            m = (r+l)//2
            if nums[m] == target:
                last_targ = m
                l = m +1
            elif nums[m] < target:
                l = m+1
            else:
                r = m - 1
        
        return [first_targ, last_targ]