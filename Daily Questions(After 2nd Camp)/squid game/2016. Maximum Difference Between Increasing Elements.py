class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        best_max = -1 * 2**31
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    best_max = max(best_max, nums[j] - nums[i])
        
        return best_max if best_max != -1 * 2**31 else -1