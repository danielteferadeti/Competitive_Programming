class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distnct = set(nums)
        
        distnct = list(distnct)
        
        distnct.sort()
        
        return distnct[-3] if len(distnct) >= 3 else distnct[-1]