class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_up_to_n = int((n*(n+1))/2)
        nums_sum = sum(nums)
        
        return sum_up_to_n - nums_sum