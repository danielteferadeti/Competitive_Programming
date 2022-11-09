class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum_should_be = n*((n+1)/2)
        cur_sum = sum(nums)
        
        duplicate_num = 0
        
        for num in nums:
            if nums[abs(num)-1] <0:
                duplicate_num = abs(num)
                break
            else:
                nums[abs(num)-1] = -1*nums[abs(num)-1]        
        
        return [duplicate_num,int(sum_should_be - (cur_sum - duplicate_num))]