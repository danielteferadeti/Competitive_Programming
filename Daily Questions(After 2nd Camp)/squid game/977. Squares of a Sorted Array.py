class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)): nums[i] = (nums[i])**2
            
        heapq.heapify(nums)
        result = []
        
        while nums: result.append(heapq.heappop(nums))
        
        return result
            