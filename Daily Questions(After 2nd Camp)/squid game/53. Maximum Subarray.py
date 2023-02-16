class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kane's algorithm
        current_sum = 0
        maxSum = float('-inf')
        
        for i in range(len(nums)):
            current_sum += nums[i]
            
            if current_sum > maxSum:
                maxSum = current_sum
                
            if current_sum < 0:
                current_sum = 0
            
        return maxSum