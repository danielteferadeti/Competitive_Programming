class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if sum(nums)==0: return 0
        
        operation = True
        num_opr = 0
        nums.sort()
        while operation:
            min_ = min(nums)
            for num in nums:
                if num >0:
                    min_= num
                    break
            num_opr +=1
            for i in range(len(nums)):
                if nums[i] > 0:
                    nums[i] -= min_
            
            if sum(nums)==0:
                operation = False
                
        return num_opr